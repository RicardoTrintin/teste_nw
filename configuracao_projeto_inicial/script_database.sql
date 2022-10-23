CREATE TABLE resumo_pedidos_cliente (
	id SERIAL, 
	cpf varchar(15),
	cnpj VARCHAR(20),
	private integer,
	incompleto integer,
	data_ultima_compra DATE, 
	ticket_medio decimal, 
	ticket_ultima_compra decimal, 
	loja_frequente VARCHAR(20), 
	loja_ultima_compra VARCHAR, 
	created_at timestamp, 
	updated_at timestamp
); 