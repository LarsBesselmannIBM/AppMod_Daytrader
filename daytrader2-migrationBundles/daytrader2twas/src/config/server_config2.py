AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:default_host/'), '[[hostname "*"] [port "19080"]]')
AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:admin_host/'), '[[hostname "*"] [port "19043"]]')
AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:default_host/'), '[[hostname "*"] [port "19081"]]')
AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:admin_host/'), '[[hostname "*"] [port "19044"]]')
AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:default_host/'), '[[hostname "*"] [port "19082"]]')
AdminConfig.create('HostAlias', AdminConfig.getid('/Cell:DefaultCell01/VirtualHost:admin_host/'), '[[hostname "*"] [port "19045"]]')
AdminConfig.save()
