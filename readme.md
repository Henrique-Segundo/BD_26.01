# Trabalho final da disciplina SMD0099 - BANCO DE DADOS I (2026.1 - T01)
## Sistema de gerenciamento diario de leitura, em Python, com integração de banco de dados PostgreSQL
### Equipe:
ARTHUR HERACLIO BARROS DE ARAUJO - 567939

DAVID BOANERGES OLIVEIRA MESQUITA - 566358

HENRIQUE SEGUNDO DA FONSECA - 566118

JOAO AMAURI RODRIGUES DO NASCIMENTO - 566937

RENAN ARAUJO POLAINAS - 566298

### Comandos SQL para popular o banco de dados para teste:
#### dados retirados do site goodreads ou criado.
INSERT INTO Genero (id,nome, descricao) VALUES 
(1,'Chick Lit', 'Chick lit is genre fiction which addresses issues of modern womanhood, often humorously and lightheartedly.'), 
(2,'Romance', 'According to the Romance Writers of America, "Two basic elements comprise every romance novel: a central love story and an emotionally-satisfying and optimistic ending."'),
(3,'Fiction', 'Fiction is the telling of stories which are not real. More specifically, fiction is an imaginative form of narrative, one of the four basic rhetorical modes'),
(4,'Fantasy','Fantasy is a genre that uses magic and other supernatural forms as a primary element of plot, theme, and/or setting.'),
(5,'Young Adult','Young-adult fiction (often abbreviated as YA) is fiction written for, published for, or marketed to adolescents and young adults, roughly ages 13 to 18.'),
(6,'Christmas','Christmas (Old English: Crīstesmæsse, meaning "Christ's Mass") is an annual commemoration of the birth of Jesus Christ and a widely observed cultural holiday, celebrated generally on December 25 by billions of people around the world. '),
(7,'Mythology','The term mythology can refer to a body of myths or to any traditional story. ');

INSERT INTO livro (id,nome, descricao, data_de_publicacao) VALUES 
(1,'Querido John', '“Querido John”, dizia a carta que partiu um coração e transformou duas vidas para sempre...' , '2006'),
(2,'A Luneta Ambar','A Luneta Âmbar fecha a trilogia. Lyra desaparece e, em seu encalço, estão: Will, que quer ajudar a amiga...','2000'),
(3,'Deixe a Neve Cair','Na noite de Natal, uma tempestade de neve transforma uma pequena cidade num inusitado refúgio para encontros românticos...','2008'),
(4,'O ladrao de raios','Primeiro volume da saga Percy Jackson e os olimpianos, O ladrão de raios esteve entre os primeiros lugares ...','2005');

INSERT INTO livroGenero (livro_id, genero_id) VALUES 
(1,1),(1,2),(1,3),
(2,4),(2,5),(2,3),
(3,6),(3,5),(3,2),
(4,4),(4,5),(4,);

INSERT INTO usuario (id, nome, descricao, data_de_nascimento) VALUES
(1,'Henrique','gosta de livros de misterio',10/12/2000),
(2,'Amauri','gosto de musica e jogos',22/10/2002),
(3,'Lucas','Prefere leituras técnicas',15/07/2002),
(4,'Eduardo', 'gosta de leituras leves e fofas',17/07/2006),
(5,'Felipe','Não gosta muito de ler',05/05/2005);

INSERT INTO Diario (livro_id, usuario_id, nota, review, data) VALUES
(3,1,4,'Gosto do primeiro conto','Ontem'),
(4,1,3,'Bem mais ou menos mas gostava na adolecencia','Faz um tempo'),
(2,2,5,'Ela é ambar','vou ler, confia'),
(4,2,2,'Eu não gostei','05/05/2015'),
(1,3,3,'foi ok','mês passado'),
(1,4,4,'Muito fofo','Eu não li na real');