[![Test](https://github.com/mtpettyp/ansible-web/actions/workflows/test.yml/badge.svg)](https://github.com/mtpettyp/ansible-web/actions/workflows/test.yml)


Web
====

Web server role


Role Variables
--------------

* `admin_email` - Email for Let's Encrypt
* `sites` - List of nginx websites to create
    * `name` - site name
    * `type` - Type of site to create (static or proxy)
    * `domains` - List of domains for this website
    * `files` - location of website files
    * `proxied_server` - Server to proxy to (only when type=proxy)


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    admin_email: admin@example.com
    sites:
      - name: example.com
        domains:
          - example.com
          - www.example.com
        files: tests/example.com/html/
        type: static
      - name: proxied.example.com
        domains:
          - proxied.example.com
        files: tests/example.com/html/
        type: proxy
        proxied_server:  http://127.0.0.1:8009/
  include_role:
    name: "ansible-web"
```

Development
-----------

uv is used to manage this project's Python dependencies

### Installation
`uv sync`

### Running
`uv run molecule test`

License
-------

MIT
