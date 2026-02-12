# 创建用户信息表

```mysql
CREATE TABLE IF NOT EXISTS `tb_user`(
    `id` int unsigned auto_increment primary key COMMENT "用户编号",
    `username` varchar(40) NOT NULL COMMENT "用户名",
    `password` varchar(128) COMMENT "密码",
    `identityType` varchar(2) COMMENT "证件类型",
    `identityNumber` varchar(20) COMMENT "证件号码",
    `mobileAreaCode` varchar(3) COMMENT "手机号码区号",
    `mobileNumber` varchar(40) COMMENT "手机号码",
    `birthday` smallint COMMENT "出生日期",
    `gender` smallint COMMENT "性别", -- 0 女性, 1 男性
    `married` smallint COMMENT "婚姻状况", -- 0 未婚, 1 已婚
    `regdate` varchar(100) COMMENT "注册日期",
    `hometown` varchar(100) COMMENT "家乡",
    `location` varchar(100) COMMENT "现居住地"
) COMMENT = "用户信息表";
```

插入测试数据

```sql
insert into `tb_user` (`username`, `password`) values
("张三", "zhangsan"),
("李四", "lisi"),
("王五", "wangwu"),
("孙六", "sunliu"),;
commit;
```

# 创建账户信息表

```mysql
CREATE TABLE IF NOT EXISTS `tb_acct`(
    `id` int unsigned auto_increment primary key COMMENT "编号",
    `custId` varchar(18) NOT NULL COMMENT "客户号",
    `accountNumber` varchar(40) NOT NULL COMMENT "账户号",
    `accountName` varchar(40) COMMENT "账户名",
    `balanceAmt` decimal(18,2) NOT NULL COMMENT "账户余额"
) COMMENT = "账户信息表";
```

```mysql
insert into `tb_acct`(`custId`, `accountNumber`, `accountName`, `balanceAmt`) values
("10001", "1001001", "测试账号一", 1000.01),
("10002", "1002001", "测试账号二", 2000.02),
("10003", "1003001", "测试账号三", 3000.03);
commit;
```

# 创建账户交易明细表

```mysql
CREATE TABLE IF NOT EXISTS `tb_acct_trans`(
    `id` int unsigned auto_increment primary key COMMENT "编号",
    `custId` varchar(18) NOT NULL COMMENT "客户号",
    `accountNumber` varchar(40) NOT NULL COMMENT "账户号",
    `accountName` varchar(40) COMMENT "账户名",
    `transAmt` decimal(18,2) NOT NULL COMMENT "交易金额",
    `balanceAmt` decimal(18,2) NOT NULL COMMENT "账户余额",
    `oppositeAccountNumber` varchar(40) NOT NULL COMMENT "交易对手账户号",
    `oppositeAccountName` varchar(40) COMMENT "交易对手账户名"
) COMMENT = "账户交易明细表";
```

```mysql
insert into `tb_acct_trans`(`custId`, `accountNumber`, `accountName`, `transAmt`, `balanceAmt`, `oppositeAccountNumber`, `oppositeAccountName`) values
("10001", "1001001", "测试账号一", 10.02, 1000.01, "1002001", "测试账号二"),
("10001", "1001001", "测试账号一", 20.03, 1000.01, "1003001", "测试账号三"),
("10001", "1002001", "测试账号二", 30.04, 1000.01, "1003001", "测试账号三");
commit;
```

