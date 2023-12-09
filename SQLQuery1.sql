CREATE TABLE Customer (
    C_ID int NOT NULL PRIMARY KEY,
    f_name varchar(255),
    l_name varchar(255),
    address varchar(5)
);

CREATE TABLE Orders (
    O_ID int NOT NULL PRIMARY KEY,
    Order_Date varchar(255),
    Departure_Time varchar(255),
    Delivered_Time varchar(255),
    C_ID int NOT NULL,
    CONSTRAINT FK_C_ID FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);

CREATE TABLE Purchase (
    P_ID int NOT NULL PRIMARY KEY,
    O_ID int NOT NULL,
    quantity int NOT NULL,
    CONSTRAINT FK_O_ID FOREIGN KEY (O_ID) REFERENCES Orders(O_ID),
    CONSTRAINT UK_Purchase_P_ID UNIQUE (P_ID)
);

CREATE TABLE Product (
    P_ID int NOT NULL PRIMARY KEY,
    name varchar(255),
    price int NOT NULL,
    distributor varchar(255),
    CONSTRAINT FK_P_ID FOREIGN KEY (P_ID) REFERENCES Purchase(P_ID)
);

CREATE TABLE Distributor (
    D_ID int NOT NULL PRIMARY KEY,
    name varchar(255),
    address varchar(255)
);
