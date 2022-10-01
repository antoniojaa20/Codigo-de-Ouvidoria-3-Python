CREATE TABLE tb_usuario (
	id int auto_increment,
    nome varchar(50),
    usuario varchar(30) unique,
    senha varchar(20),
    primary key(id)
);

CREATE TABLE tb_elogio (
	id int auto_increment,
    elogio text,
    usuario_id int,
    primary key(id),
    foreign key (usuario_id) references tb_usuario(id)
);

CREATE TABLE tb_reclamacao (
	id int auto_increment,
    reclamacao text,
    usuario_id int,
    primary key(id),
    foreign key (usuario_id) references tb_usuario(id)
);