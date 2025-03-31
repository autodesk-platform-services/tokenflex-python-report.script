#####################################################################
## Copyright (c) Autodesk, Inc. All rights reserved
## Written by APS Partner Development
##
## Permission to use, copy, modify, and distribute this software in
## object code form for any purpose and without fee is hereby granted,
## provided that the above copyright notice appears in all copies and
## that both that copyright notice and the limited warranty and
## restricted rights notice below appear in all supporting
## documentation.
##
## AUTODESK PROVIDES THIS PROGRAM "AS IS" AND WITH ALL FAULTS.
## AUTODESK SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTY OF
## MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE.  AUTODESK, INC.
## DOES NOT WARRANT THAT THE OPERATION OF THE PROGRAM WILL BE
## UNINTERRUPTED OR ERROR FREE.
#####################################################################

import os
from urllib.parse import urljoin
access_token_url = os.getenv(
    'APS_TOKEN_URL',
    'https://developer.api.autodesk.com/authentication/v2/token')
base_url = os.getenv('APS_BASE_URL', 'https://developer.api.autodesk.com')
base_tokenflex_api = os.getenv(
    'APS_TOKENFLEX_URL',
    'https://developer.api.autodesk.com/tokenflex/')
authorize_url = os.getenv('APS_AUTH_URL', 'https://developer.api.autodesk.com/authentication/v2/authorize')
