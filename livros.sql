--
-- PostgreSQL database dump
--

\restrict NGfJbMp3PGPhNqqE5vByyJngjmqgCcKWoamrMuYRMebcoUVasFtFU3IKfW844KG

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-06-22 22:25:14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 16450)
-- Name: diario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diario (
    data date NOT NULL,
    nota numeric NOT NULL,
    review character varying,
    livro_id integer NOT NULL,
    usuario_id integer NOT NULL
);


ALTER TABLE public.diario OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16459)
-- Name: diario_livro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.diario_livro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.diario_livro_id_seq OWNER TO postgres;

--
-- TOC entry 5059 (class 0 OID 0)
-- Dependencies: 220
-- Name: diario_livro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.diario_livro_id_seq OWNED BY public.diario.livro_id;


--
-- TOC entry 221 (class 1259 OID 16460)
-- Name: diario_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.diario_usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.diario_usuario_id_seq OWNER TO postgres;

--
-- TOC entry 5060 (class 0 OID 0)
-- Dependencies: 221
-- Name: diario_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.diario_usuario_id_seq OWNED BY public.diario.usuario_id;


--
-- TOC entry 222 (class 1259 OID 16461)
-- Name: genero; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genero (
    nome character varying NOT NULL,
    descricao character varying,
    id integer NOT NULL
);


ALTER TABLE public.genero OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16468)
-- Name: genero_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.genero_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.genero_id_seq OWNER TO postgres;

--
-- TOC entry 5061 (class 0 OID 0)
-- Dependencies: 223
-- Name: genero_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.genero_id_seq OWNED BY public.genero.id;


--
-- TOC entry 224 (class 1259 OID 16469)
-- Name: livro_genero; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livro_genero (
    livro_id integer NOT NULL,
    genero_id integer NOT NULL
);


ALTER TABLE public.livro_genero OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16474)
-- Name: livro_genero_genero_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_genero_genero_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.livro_genero_genero_id_seq OWNER TO postgres;

--
-- TOC entry 5062 (class 0 OID 0)
-- Dependencies: 225
-- Name: livro_genero_genero_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livro_genero_genero_id_seq OWNED BY public.livro_genero.genero_id;


--
-- TOC entry 226 (class 1259 OID 16475)
-- Name: livro_genero_livro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livro_genero_livro_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.livro_genero_livro_id_seq OWNER TO postgres;

--
-- TOC entry 5063 (class 0 OID 0)
-- Dependencies: 226
-- Name: livro_genero_livro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livro_genero_livro_id_seq OWNED BY public.livro_genero.livro_id;


--
-- TOC entry 227 (class 1259 OID 16476)
-- Name: livros; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.livros (
    nome character varying NOT NULL,
    descricao character varying,
    id integer NOT NULL,
    data_de_publicacao character varying NOT NULL
);


ALTER TABLE public.livros OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 16483)
-- Name: livros_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.livros_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.livros_id_seq OWNER TO postgres;

--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 228
-- Name: livros_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.livros_id_seq OWNED BY public.livros.id;


--
-- TOC entry 229 (class 1259 OID 16484)
-- Name: usuario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuario (
    nome character varying NOT NULL,
    descricao character varying,
    data_de_nascimento date NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 16492)
-- Name: usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuario_id_seq OWNER TO postgres;

--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 230
-- Name: usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuario_id_seq OWNED BY public.usuario.id;


--
-- TOC entry 4878 (class 2604 OID 16493)
-- Name: diario livro_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diario ALTER COLUMN livro_id SET DEFAULT nextval('public.diario_livro_id_seq'::regclass);


--
-- TOC entry 4879 (class 2604 OID 16494)
-- Name: diario usuario_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diario ALTER COLUMN usuario_id SET DEFAULT nextval('public.diario_usuario_id_seq'::regclass);


--
-- TOC entry 4880 (class 2604 OID 16495)
-- Name: genero id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genero ALTER COLUMN id SET DEFAULT nextval('public.genero_id_seq'::regclass);


--
-- TOC entry 4881 (class 2604 OID 16496)
-- Name: livro_genero livro_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_genero ALTER COLUMN livro_id SET DEFAULT nextval('public.livro_genero_livro_id_seq'::regclass);


--
-- TOC entry 4882 (class 2604 OID 16497)
-- Name: livro_genero genero_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_genero ALTER COLUMN genero_id SET DEFAULT nextval('public.livro_genero_genero_id_seq'::regclass);


--
-- TOC entry 4883 (class 2604 OID 16498)
-- Name: livros id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livros ALTER COLUMN id SET DEFAULT nextval('public.livros_id_seq'::regclass);


--
-- TOC entry 4884 (class 2604 OID 16499)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public.usuario_id_seq'::regclass);


--
-- TOC entry 5042 (class 0 OID 16450)
-- Dependencies: 219
-- Data for Name: diario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.diario VALUES ('2026-01-01', 4, 'Gosto do primeiro conto', 3, 1);
INSERT INTO public.diario VALUES ('2026-02-02', 3, 'Bem mais ou menos mas gostava na adolecencia', 4, 1);
INSERT INTO public.diario VALUES ('2026-03-03', 5, 'Ela é ambar', 2, 2);
INSERT INTO public.diario VALUES ('2026-04-04', 2, 'Eu não gostei', 4, 2);
INSERT INTO public.diario VALUES ('2026-05-05', 3, 'foi ok', 1, 3);
INSERT INTO public.diario VALUES ('2026-06-06', 4, 'Muito fofo', 1, 4);


--
-- TOC entry 5045 (class 0 OID 16461)
-- Dependencies: 222
-- Data for Name: genero; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.genero VALUES ('Chick Lit', 'Chick lit is genre fiction which addresses issues of modern womanhood, often humorously and lightheartedly.', 1);
INSERT INTO public.genero VALUES ('Romance', 'According to the Romance Writers of America, "Two basic elements comprise every romance novel: a central love story and an emotionally-satisfying and optimistic ending."', 2);
INSERT INTO public.genero VALUES ('Fiction', 'Fiction is the telling of stories which are not real. More specifically, fiction is an imaginative form of narrative, one of the four basic rhetorical modes', 3);
INSERT INTO public.genero VALUES ('Fantasy', 'Fantasy is a genre that uses magic and other supernatural forms as a primary element of plot, theme, and/or setting.', 4);
INSERT INTO public.genero VALUES ('Young Adult', 'Young-adult fiction (often abbreviated as YA) is fiction written for, published for, or marketed to adolescents and young adults, roughly ages 13 to 18.', 5);
INSERT INTO public.genero VALUES ('Christmas', 'Christmas (Old English: Crīstesmæsse, meaning "Christ`s Mass") is an annual commemoration of the birth of Jesus Christ and a widely observed cultural holiday, celebrated generally on December 25 by billions of people around the world. ', 6);
INSERT INTO public.genero VALUES ('Mythology', 'The term mythology can refer to a body of myths or to any traditional story. ', 7);


--
-- TOC entry 5047 (class 0 OID 16469)
-- Dependencies: 224
-- Data for Name: livro_genero; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 5050 (class 0 OID 16476)
-- Dependencies: 227
-- Data for Name: livros; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.livros VALUES ('Querido John', '“Querido John”, dizia a carta que partiu um coração e transformou duas vidas para sempre...', 1, '2006');
INSERT INTO public.livros VALUES ('A Luneta Ambar', 'A Luneta Âmbar fecha a trilogia. Lyra desaparece e, em seu encalço, estão: Will, que quer ajudar a amiga...', 2, '2000');
INSERT INTO public.livros VALUES ('Deixe a Neve Cair', 'Na noite de Natal, uma tempestade de neve transforma uma pequena cidade num inusitado refúgio para encontros românticos...', 3, '2008');
INSERT INTO public.livros VALUES ('O ladrao de raios', 'Primeiro volume da saga Percy Jackson e os olimpianos, O ladrão de raios esteve entre os primeiros lugares...', 4, '2005');


--
-- TOC entry 5052 (class 0 OID 16484)
-- Dependencies: 229
-- Data for Name: usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.usuario VALUES ('Henrique', 'gosta de livros de misterio', '2000-12-10', 1);
INSERT INTO public.usuario VALUES ('Amauri', 'gosto de musica e jogos', '2002-10-22', 2);
INSERT INTO public.usuario VALUES ('Lucas', 'Prefere leituras técnicas', '2002-07-15', 3);
INSERT INTO public.usuario VALUES ('Eduardo', 'gosta de leituras leves e fofas', '2006-07-17', 4);
INSERT INTO public.usuario VALUES ('Felipe', 'Não gosta muito de ler', '2005-05-05', 5);


--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 220
-- Name: diario_livro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.diario_livro_id_seq', 1, false);


--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 221
-- Name: diario_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.diario_usuario_id_seq', 1, false);


--
-- TOC entry 5068 (class 0 OID 0)
-- Dependencies: 223
-- Name: genero_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.genero_id_seq', 1, false);


--
-- TOC entry 5069 (class 0 OID 0)
-- Dependencies: 225
-- Name: livro_genero_genero_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livro_genero_genero_id_seq', 1, false);


--
-- TOC entry 5070 (class 0 OID 0)
-- Dependencies: 226
-- Name: livro_genero_livro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livro_genero_livro_id_seq', 1, false);


--
-- TOC entry 5071 (class 0 OID 0)
-- Dependencies: 228
-- Name: livros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.livros_id_seq', 1, false);


--
-- TOC entry 5072 (class 0 OID 0)
-- Dependencies: 230
-- Name: usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuario_id_seq', 1, false);


--
-- TOC entry 4886 (class 2606 OID 16501)
-- Name: diario diario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diario
    ADD CONSTRAINT diario_pkey PRIMARY KEY (livro_id, usuario_id);


--
-- TOC entry 4888 (class 2606 OID 16503)
-- Name: genero genero_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genero
    ADD CONSTRAINT genero_pkey PRIMARY KEY (id);


--
-- TOC entry 4890 (class 2606 OID 16505)
-- Name: livro_genero livro_genero_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livro_genero
    ADD CONSTRAINT livro_genero_pkey PRIMARY KEY (livro_id, genero_id);


--
-- TOC entry 4892 (class 2606 OID 16507)
-- Name: livros livros_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_pkey PRIMARY KEY (id);


--
-- TOC entry 4894 (class 2606 OID 16509)
-- Name: usuario usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id);


-- Completed on 2026-06-22 22:25:15

--
-- PostgreSQL database dump complete
--

\unrestrict NGfJbMp3PGPhNqqE5vByyJngjmqgCcKWoamrMuYRMebcoUVasFtFU3IKfW844KG

