class Table:
    def __init__(self):
        self.Tables = {}

    def createTables(self):
        self.productTable()
        self.transectionTable()
        self.balanceTable()

        

    def productTable(self):
        self.Tables['products'] = (
            "  CREATE TABLE `products` ("
            " `id` INT(11) NOT NULL AUTO_INCREMENT,"
            " `name` VARCHAR(255) NOT NULL,"
            " `buyPrice` INT(11) NOT NULL,"
            " `sellPrice` INT(11) NOT NULL,"
            " `profit` INT(11) NOT NULL,"
            " `quantity` INT(11) NOT NULL,"
            " `status` TINYINT(1) NOT NULL,"
            " `created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB"
        )

    def transectionTable(self):
        self.Tables['transections'] = (
            "  CREATE TABLE `transections` ("
            " `id` INT(11) NOT NULL AUTO_INCREMENT,"
            " `name` VARCHAR(255) NOT NULL,"
            " `type` VARCHAR(255) NOT NULL,"
            " `quantity` INT(11) NOT NULL,"
            " `created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB"
        )

    def balanceTable(self):
        self.Tables['balance'] = (
            "  CREATE TABLE `balance` ("
            " `id` INT(11) NOT NULL AUTO_INCREMENT,"
            " `type` VARCHAR(255) NOT NULL,"
            " `profit` INT(11) NOT NULL,"
            " `balance` INT(11) NOT NULL,"
            " `created` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB"
        )
