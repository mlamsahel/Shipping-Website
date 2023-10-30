Create Table Customer(
	C_ID int NOT NULL PRIMARY KEY,
	f_name varchar(255),
	l_name varchar(255),
	address num(5),
);
Create Table Order(
	O_ID int NOT NULL PRIMARY KEY,
	Order_Date varchar(255),
	Departure_Time varchar(255),
	Delivered_Time varchar(255),
	C_ID int NOT NULL,
 CONSTRAINT FK_C_ID FOREIGN KEY (C_ID)
 REFERENCES Customer(C_ID)
);
Create Table Purchase(
	P_ID int NOT NULL,
	O_ID int NOT NULL,
	quantity int NOT NULL,
	CONSTRAINT FK_O_ID FOREIGN KEY (O_ID),
	REFERENCES Order(O_ID),
	PRIMARY KEY (O_ID, C_ID),
);
Create Table Product(
	P_ID int NOT NULL,
	name varchar(255),
	price int NOT NULL,
	distributor varchar(255),
	CONSTRAINT FK_P_ID FOREIGN KEY (P_ID)
	REFERENCES Purchase(P_ID),
	PRIMARY KEY (P_ID),
);
Create Table Distributer(
	D_ID int NOT NULL PRIMARY KEY,
	name varchar(255),
	address varchar(255),
);
