#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from ispw.ISPWClientUtil import ISPWClientUtil

ispw_client = ISPWClientUtil.create_ispw_client(ispwServiceServer, username, password)

ispw_client.create_release(release_id=relid, application=application, stream=stream, release_description=description, user=user)