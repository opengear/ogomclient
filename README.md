# Operations Manager API Client

The client is tightly tied to the Operations Manager RESTful API RAML specification, which can be found [here](http://ftp.opengear.com/download/api/operations_manager/).

## Authentication

The **Operations Manager API Client** expects the following environment variables:

- **(required)** `OGOM_API_USER` a valid Operations Manager user
- **(required)** `OGOM_API_PASS` a valid Operations Manager user's password
- **(required)** `OGOM_API_URL` the Operations Manager API URL without `/api/v2.2`

They can be combined with optional parameters at instantiation:

```python
api = OperationsManagerClient(url = "https://192.168.0.11",
                         username = "root",
                         password = "myP@ssw0rd")
```

## Conventions

All the methods follow the convention that a call to an URL like:

```
GET /system/webui_session_timeout HTTP/1.0
```

would be performed through the client as:

```python
>>> from ogomclient import OperationsManagerClient
>>> api = OperationsManagerClient()
>>> client = api.get_client()
>>> client.system.webui_session_timeout.get()
```

Basically, all `/` are replaced by `.` followed by an action as specified below.

#### GET: `find()`
Used when asking for a specific object.

Example:

```
GET /groups/groups-2 HTTP/1.0
```

becomes:

```python
user_group = client.groups.find(id='groups-2')
```

or

```python
user_group = client.groups.find('groups-2')
```

In case of a child object like in `/ports/{id}/sessions/{pid}`, with a possible call like:

```
GET /ports/ports-14/sessions/719 HTTP/1.0
```

the Python call should be:


```python
session = client.ports.sessions.find(id='719', parent_id='ports-14')
```

It is also possible to use:

```python
session = client.ports.sessions.find(id='719', port_id='ports-14')
```

Always paying attention to the simple plural formatting removal:

- **ports**: *port*
- **properties**: *property*

### GET: `list()`
Used when asking for a list of objects.

Example:

```
GET /ports HTTP/1.0
```

becomes:

```python
ports = client.ports.list()
```

Parameters may apply, like `searchparameters`, `logLines`, and so on:

```python
ports = client.ports.list(searchparameters='config:mode=disabled')
```

### GET: `get()`
Only used when the two previous do not apply, like:

```
GET /system/cli_session_timeout HTTP/1.0
```

which becomes:

```python
timeout = client.system.cli_session_timeout.get()
```

### POST: `create()`
It is used to create objects or trigger actions, for instance:

```
POST /ports/auto_discover HTTP/1.0
Content-Type: application/json
{"auto_discover": {"ports": [10, 33]}}
```

could be performed as:

```python
data = {
  "auto_discover": {
    "ports": [
      10,
      33,
    ]
  }
}
result = client.ports.auto_discover.create(data)
```

### PUT: `update()`
It is used to update a given object.

Example:

```
PUT /firewall/services/firewall_services-2 HTTP/1.0
Content-Type: application/json
{"firewall_service": {"name": "telnet", "label": "TELNET", "ports": [{"protocol": "tcp", "port": 23}]}}
```

is performed as:

```python
data = {
  "firewall_service": {
    "name": "telnet",
    "label": "TELNET",
    "ports": [
      {
        "protocol": "tcp",
        "port": 23
      }
    ]
  }
}
result = client.firewall.services.update(id='firewall_services-2', data=data)
```

### DELETE: `delete()`
It is used to delete an object by its `id`, for instance:

```
DELETE /conns/system_net_conns-8 HTTP/1.0
```

is performed as:

```python
result = client.conns.delete(id='system_net_conns-8')
```
