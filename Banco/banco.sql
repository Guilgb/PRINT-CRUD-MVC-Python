PGDMP         $                {            PRINT    15.1    15.1 E    P           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            Q           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            R           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            S           1262    16566    PRINT    DATABASE     ~   CREATE DATABASE "PRINT" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "PRINT";
                postgres    false            ?            1259    16661    agendamento    TABLE     ?   CREATE TABLE public.agendamento (
    id integer NOT NULL,
    data character varying(10) NOT NULL,
    horario time without time zone NOT NULL,
    "observação" text,
    funcionarioid integer NOT NULL
);
    DROP TABLE public.agendamento;
       public         heap    postgres    false            ?            1259    16660    agendamento_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.agendamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.agendamento_id_seq;
       public          postgres    false    221            T           0    0    agendamento_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.agendamento_id_seq OWNED BY public.agendamento.id;
          public          postgres    false    220            ?            1259    16642    animal    TABLE     V  CREATE TABLE public.animal (
    id integer NOT NULL,
    nome character varying(80) NOT NULL,
    especie character varying(50) NOT NULL,
    sexo character varying(20) NOT NULL,
    raca character varying(30) NOT NULL,
    peso character varying(5) NOT NULL,
    nascimento character varying(10) NOT NULL,
    clienteid integer NOT NULL
);
    DROP TABLE public.animal;
       public         heap    postgres    false            ?            1259    16641    animal_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.animal_id_seq;
       public          postgres    false    217            U           0    0    animal_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.animal_id_seq OWNED BY public.animal.id;
          public          postgres    false    216            ?            1259    16631    cliente    TABLE     ?  CREATE TABLE public.cliente (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cpf character varying(11) NOT NULL,
    nascimento character varying(10) NOT NULL,
    telefone character varying(10) NOT NULL,
    email character varying(50),
    rua character varying(100) NOT NULL,
    bairro character varying(80) NOT NULL,
    numero character varying(5) NOT NULL
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            ?            1259    16630    cliente_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.cliente_id_seq;
       public          postgres    false    215            V           0    0    cliente_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.cliente_id_seq OWNED BY public.cliente.id;
          public          postgres    false    214            ?            1259    16654    funcionario    TABLE       CREATE TABLE public.funcionario (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    nascimento character varying(15) NOT NULL,
    email character varying(50) NOT NULL,
    telefone character varying(15) NOT NULL,
    cargo character varying(30) NOT NULL
);
    DROP TABLE public.funcionario;
       public         heap    postgres    false            ?            1259    16653    funcionario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.funcionario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.funcionario_id_seq;
       public          postgres    false    219            W           0    0    funcionario_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.funcionario_id_seq OWNED BY public.funcionario.id;
          public          postgres    false    218            ?            1259    16722    pertence    TABLE     c   CREATE TABLE public.pertence (
    vacinaid integer NOT NULL,
    prontuarioid integer NOT NULL
);
    DROP TABLE public.pertence;
       public         heap    postgres    false            ?            1259    16674    possui    TABLE     b   CREATE TABLE public.possui (
    animalid integer NOT NULL,
    agendamentoid integer NOT NULL
);
    DROP TABLE public.possui;
       public         heap    postgres    false            ?            1259    16699 
   prontuario    TABLE     P  CREATE TABLE public.prontuario (
    id integer NOT NULL,
    raca character varying(20) NOT NULL,
    data character varying(15) NOT NULL,
    especie character varying(20) NOT NULL,
    porte character varying(20) NOT NULL,
    sexo character varying(15) NOT NULL,
    animalid integer NOT NULL,
    veterinarioid integer NOT NULL
);
    DROP TABLE public.prontuario;
       public         heap    postgres    false            ?            1259    16698    prontuario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.prontuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.prontuario_id_seq;
       public          postgres    false    226            X           0    0    prontuario_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.prontuario_id_seq OWNED BY public.prontuario.id;
          public          postgres    false    225            ?            1259    16716    vacina    TABLE     ?   CREATE TABLE public.vacina (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    validade character varying(10) NOT NULL,
    fabricante character varying(150) NOT NULL,
    volume character varying(15) NOT NULL
);
    DROP TABLE public.vacina;
       public         heap    postgres    false            ?            1259    16715    vacina_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.vacina_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.vacina_id_seq;
       public          postgres    false    228            Y           0    0    vacina_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.vacina_id_seq OWNED BY public.vacina.id;
          public          postgres    false    227            ?            1259    16688    veterinario    TABLE     D  CREATE TABLE public.veterinario (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cpf character varying(11) NOT NULL,
    nascimento character varying(10) NOT NULL,
    telefone character varying(12) NOT NULL,
    email character varying(100) NOT NULL,
    formacao character varying(100) NOT NULL
);
    DROP TABLE public.veterinario;
       public         heap    postgres    false            ?            1259    16687    veterinario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.veterinario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.veterinario_id_seq;
       public          postgres    false    224            Z           0    0    veterinario_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.veterinario_id_seq OWNED BY public.veterinario.id;
          public          postgres    false    223            ?           2604    16934    agendamento id    DEFAULT     p   ALTER TABLE ONLY public.agendamento ALTER COLUMN id SET DEFAULT nextval('public.agendamento_id_seq'::regclass);
 =   ALTER TABLE public.agendamento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            ?           2604    16935 	   animal id    DEFAULT     f   ALTER TABLE ONLY public.animal ALTER COLUMN id SET DEFAULT nextval('public.animal_id_seq'::regclass);
 8   ALTER TABLE public.animal ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            ?           2604    16936 
   cliente id    DEFAULT     h   ALTER TABLE ONLY public.cliente ALTER COLUMN id SET DEFAULT nextval('public.cliente_id_seq'::regclass);
 9   ALTER TABLE public.cliente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            ?           2604    16937    funcionario id    DEFAULT     p   ALTER TABLE ONLY public.funcionario ALTER COLUMN id SET DEFAULT nextval('public.funcionario_id_seq'::regclass);
 =   ALTER TABLE public.funcionario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            ?           2604    16938    prontuario id    DEFAULT     n   ALTER TABLE ONLY public.prontuario ALTER COLUMN id SET DEFAULT nextval('public.prontuario_id_seq'::regclass);
 <   ALTER TABLE public.prontuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            ?           2604    16939 	   vacina id    DEFAULT     f   ALTER TABLE ONLY public.vacina ALTER COLUMN id SET DEFAULT nextval('public.vacina_id_seq'::regclass);
 8   ALTER TABLE public.vacina ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    227    228    228            ?           2604    16940    veterinario id    DEFAULT     p   ALTER TABLE ONLY public.veterinario ALTER COLUMN id SET DEFAULT nextval('public.veterinario_id_seq'::regclass);
 =   ALTER TABLE public.veterinario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            E          0    16661    agendamento 
   TABLE DATA           W   COPY public.agendamento (id, data, horario, "observação", funcionarioid) FROM stdin;
    public          postgres    false    221   ?P       A          0    16642    animal 
   TABLE DATA           \   COPY public.animal (id, nome, especie, sexo, raca, peso, nascimento, clienteid) FROM stdin;
    public          postgres    false    217   ?P       ?          0    16631    cliente 
   TABLE DATA           b   COPY public.cliente (id, nome, cpf, nascimento, telefone, email, rua, bairro, numero) FROM stdin;
    public          postgres    false    215   gQ       C          0    16654    funcionario 
   TABLE DATA           S   COPY public.funcionario (id, nome, nascimento, email, telefone, cargo) FROM stdin;
    public          postgres    false    219   R       M          0    16722    pertence 
   TABLE DATA           :   COPY public.pertence (vacinaid, prontuarioid) FROM stdin;
    public          postgres    false    229   ER       F          0    16674    possui 
   TABLE DATA           9   COPY public.possui (animalid, agendamentoid) FROM stdin;
    public          postgres    false    222   bR       J          0    16699 
   prontuario 
   TABLE DATA           c   COPY public.prontuario (id, raca, data, especie, porte, sexo, animalid, veterinarioid) FROM stdin;
    public          postgres    false    226   R       L          0    16716    vacina 
   TABLE DATA           H   COPY public.vacina (id, nome, validade, fabricante, volume) FROM stdin;
    public          postgres    false    228   ?R       H          0    16688    veterinario 
   TABLE DATA           [   COPY public.veterinario (id, nome, cpf, nascimento, telefone, email, formacao) FROM stdin;
    public          postgres    false    224   ?R       [           0    0    agendamento_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.agendamento_id_seq', 1, true);
          public          postgres    false    220            \           0    0    animal_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.animal_id_seq', 5, true);
          public          postgres    false    216            ]           0    0    cliente_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.cliente_id_seq', 35, true);
          public          postgres    false    214            ^           0    0    funcionario_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.funcionario_id_seq', 5, true);
          public          postgres    false    218            _           0    0    prontuario_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.prontuario_id_seq', 1, true);
          public          postgres    false    225            `           0    0    vacina_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.vacina_id_seq', 1, true);
          public          postgres    false    227            a           0    0    veterinario_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.veterinario_id_seq', 1, true);
          public          postgres    false    223            ?           2606    16668    agendamento agendamento_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT agendamento_pkey;
       public            postgres    false    221            ?           2606    16647    animal animal_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.animal DROP CONSTRAINT animal_pkey;
       public            postgres    false    217            ?           2606    16638    cliente cliente_cpf_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_cpf_key UNIQUE (cpf);
 A   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_cpf_key;
       public            postgres    false    215            ?           2606    16640    cliente cliente_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_email_key;
       public            postgres    false    215            ?           2606    16636    cliente cliente_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pkey;
       public            postgres    false    215            ?           2606    16659    funcionario funcionario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.funcionario DROP CONSTRAINT funcionario_pkey;
       public            postgres    false    219            ?           2606    16704    prontuario prontuario_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT prontuario_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT prontuario_pkey;
       public            postgres    false    226            ?           2606    16721    vacina vacina_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.vacina
    ADD CONSTRAINT vacina_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.vacina DROP CONSTRAINT vacina_pkey;
       public            postgres    false    228            ?           2606    16695    veterinario veterinario_cpf_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_cpf_key UNIQUE (cpf);
 I   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_cpf_key;
       public            postgres    false    224            ?           2606    16697 !   veterinario veterinario_email_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_email_key UNIQUE (email);
 K   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_email_key;
       public            postgres    false    224            ?           2606    16693    veterinario veterinario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_pkey;
       public            postgres    false    224            ?           2606    16682    possui id_fk_agendamento    FK CONSTRAINT     ?   ALTER TABLE ONLY public.possui
    ADD CONSTRAINT id_fk_agendamento FOREIGN KEY (agendamentoid) REFERENCES public.agendamento(id) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.possui DROP CONSTRAINT id_fk_agendamento;
       public          postgres    false    3229    222    221            ?           2606    16677    possui id_fk_animal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.possui
    ADD CONSTRAINT id_fk_animal FOREIGN KEY (animalid) REFERENCES public.animal(id) ON DELETE CASCADE;
 =   ALTER TABLE ONLY public.possui DROP CONSTRAINT id_fk_animal;
       public          postgres    false    217    222    3225            ?           2606    16705    prontuario id_fk_animal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT id_fk_animal FOREIGN KEY (animalid) REFERENCES public.animal(id) ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT id_fk_animal;
       public          postgres    false    226    217    3225            ?           2606    16648    animal id_fk_cliente    FK CONSTRAINT     ?   ALTER TABLE ONLY public.animal
    ADD CONSTRAINT id_fk_cliente FOREIGN KEY (clienteid) REFERENCES public.cliente(id) ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.animal DROP CONSTRAINT id_fk_cliente;
       public          postgres    false    215    3223    217            ?           2606    16669    agendamento id_fk_funcionario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT id_fk_funcionario FOREIGN KEY (funcionarioid) REFERENCES public.funcionario(id) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT id_fk_funcionario;
       public          postgres    false    3227    219    221            ?           2606    16730    pertence id_fk_prontuario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.pertence
    ADD CONSTRAINT id_fk_prontuario FOREIGN KEY (prontuarioid) REFERENCES public.prontuario(id) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.pertence DROP CONSTRAINT id_fk_prontuario;
       public          postgres    false    229    3237    226            ?           2606    16725    pertence id_fk_vacina    FK CONSTRAINT     ?   ALTER TABLE ONLY public.pertence
    ADD CONSTRAINT id_fk_vacina FOREIGN KEY (vacinaid) REFERENCES public.vacina(id) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.pertence DROP CONSTRAINT id_fk_vacina;
       public          postgres    false    3239    228    229            ?           2606    16710    prontuario id_fk_veterinario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT id_fk_veterinario FOREIGN KEY (veterinarioid) REFERENCES public.veterinario(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT id_fk_veterinario;
       public          postgres    false    224    3235    226            E      x?????? ? ?      A   _   x?3????MUp???M??L-.HM?L?,N???,JLN?44?3??K,N??M?+?򹌰h1i1jI4i1Ah???I?bB?Sҵ???%F??? ?O\?      ?   ?   x?U?K
?@??u?aĤx/?f??????f#???g.?5h{???g?5????{oAQS.4?Dϔ?????N??D?JJ?@H? |?PP'T@TR@????Šmj?6h#?6^֟^??'wpwrp?ǅ??1H      C   4   x?3????M??K,N??M?+??L?M???,I?IM??K?LN,J??????? V?X      M      x?????? ? ?      F      x?????? ? ?      J      x?????? ? ?      L   4   x?3????MKL??K?,??LILI?LKL*?LN?+I?,??)?M?????? Y??      H   -   x?3?,K-I?L.H??K,?,I???M??)???
@I?=... b     