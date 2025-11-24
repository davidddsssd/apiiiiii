create if not exists addressers(
    id integer AUTO_INCREMENT,
    street varchar (30) no null,
    suit varchar ()
);





create if not exists companies(
    name varchar(30) not null,
    catchphrase varchar (255) not null,
    bs varchar(100) not null,

    constraint pk_comapanies primary key (id)
);

create table if not exists users(
    id integer AUTO_INCREMENT,
    name varchar(30) not null,
    username varchar(15) not null,
    email varchar(255) not null,
    phone varchar(25) not null,
    website varchar(255) not null,
    addresiid integer not null,
    companyid integer no null,
    constraint pk_user  primary key (id)
    constraint fk_users_comapies foreign key (companyid)
    references companies(id)
);


create table if not exists posts(
    id integer AUTO_INCREMENT,
    title varchar(50) not null,
    body varchar(255) NOT NULL, 
    userid integer not null,
    
    constraint pk_posts primary key (id),
    constraint fk_posts_users foreign key (userid)
    references users(id)
);