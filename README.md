[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-web.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-web)


Web
====

Web server role


Role Variables
--------------

* `admin_email` - Email for Let's Encrypt
* `sites` - List of nginx websites to create
    * `name` - site name
    * `domains` - List of domains for this website
    * `files` - location of website files


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
  include_role:
    name: "ansible-web"
```

License
-------

MIT

