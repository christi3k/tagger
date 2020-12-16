#
# Copyright (c) 2020 it-eXperts IT-Dienstleistungs GmbH.
#
# This file is part of tagger
# (see https://github.com/IT-EXPERTS-AT/tagger).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import logging
from typing import List
import time

import skew as skew

from taggercore.config import ensure_config_is_set
from taggercore.manipulation import ArnManipulationStrategyFactory
from taggercore.model import Resource
from taggercore.scanner import create_resource, sort_resources
from taggercore.scanner.global_scanner import GLOBAL_SERVICES

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class RegionScanner:
    def __init__(self, region: str):
        """

        :param region: AWS region code (https://docs.aws.amazon.com/general/latest/gr/rande.html for a full list)
        """
        self._region = region

    @ensure_config_is_set
    def scan(self, resource_types_to_exclude: List[str]) -> List[Resource]:
        """

        :param resource_types_to_exclude: resource types which should not be included in the returned resources
        types are specified as they appear in the ARN pattern e.g. 'restapi'. See the 'type' attribute in the
        individual resource classes (https://github.com/tobHai/skew/tree/develop/skew/resources/aws)
        :return:
        """
        resources = self._scan_region(resource_types_to_exclude)
        # print(resources)
        resources_with_manipulated_arns = (
            self.manipulate_arn(resource) for resource in resources
        )
        return list(resources_with_manipulated_arns)

    def _scan_region(self, resource_types_to_exclude: List[str]) -> List[Resource]:
        arn = skew.ARN()
        print(f"arn: {arn}")
        logger.info("Starting to scan in region {}".format(self._region))
        # print('scanning region')
        all_scanned_resources = []

        for service in arn.service.choices():
            print(f"service: {service}.")
            if service in GLOBAL_SERVICES or service == 'cloudwatch':
                continue
            service_uri = "arn:aws:" + service + ":" + self._region + ":*:*/*"
            resources = skew.scan(service_uri)
            logger.info(f"Scanning {service_uri}")
            # print(f"resources: {resources}")
            for resource in resources:
                print(f"resource: {resource}")
                if resource.resourcetype in resource_types_to_exclude:
                    continue
                created_resource = create_resource(resource)
                if created_resource is not None:
                    all_scanned_resources.append(created_resource)
                # time.sleep(1)
        logger.info("Scanning completed for region {}".format(self._region))
        return sort_resources(all_scanned_resources)

    @staticmethod
    def manipulate_arn(resource: Resource) -> Resource:
        arn_manipulation = (
            ArnManipulationStrategyFactory.manipulation_strategy_for_service(
                resource.service
            )
        )
        resource.arn = arn_manipulation.manipulate_arn(arn=resource.arn)
        return resource
