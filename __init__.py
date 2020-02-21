"""
Opengear Operations Manager API Client

Usage:
>>> from ogomclient import OperationsManagerClient
>>> api = OperationsManagerClient()
>>> client = api.get_client()

Then, to execute GET /system/webui_session_timeout HTTP/1.0
>>> timeout = client.system.webui_session_timeout.get()

Check documentation at https://github.com/opengear/ogomclient
"""

from .ogomclient import OperationsManagerClient
