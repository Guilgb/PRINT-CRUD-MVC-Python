PGDMP         3                {            PRINTDB    15.1    15.1 F    Q           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            R           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            S           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            T           1262    16736    PRINTDB    DATABASE     ?   CREATE DATABASE "PRINTDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "PRINTDB";
                postgres    false            ?            1259    16855    agendamento    TABLE     ?   CREATE TABLE public.agendamento (
    id integer NOT NULL,
    "observação" text,
    animalid integer NOT NULL,
    funcionarioid integer NOT NULL,
    dia character(100) NOT NULL,
    momento character(100) NOT NULL
);
    DROP TABLE public.agendamento;
       public         heap    postgres    false            ?            1259    16854    agendamento_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.agendamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.agendamento_id_seq;
       public          postgres    false    221            U           0    0    agendamento_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.agendamento_id_seq OWNED BY public.agendamento.id;
          public          postgres    false    220            ?            1259    16813    animal    TABLE     V  CREATE TABLE public.animal (
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
       public         heap    postgres    false            ?            1259    16812    animal_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.animal_id_seq;
       public          postgres    false    217            V           0    0    animal_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.animal_id_seq OWNED BY public.animal.id;
          public          postgres    false    216            ?            1259    16802    cliente    TABLE     ?  CREATE TABLE public.cliente (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cpf character varying(20) NOT NULL,
    nascimento character varying(100) NOT NULL,
    telefone character varying(20) NOT NULL,
    email character varying(100),
    rua character varying(100) NOT NULL,
    bairro character varying(80) NOT NULL,
    numero character varying(100) NOT NULL
);
    DROP TABLE public.cliente;
       public         heap    postgres    false            ?            1259    16801    cliente_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.cliente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.cliente_id_seq;
       public          postgres    false    215            W           0    0    cliente_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.cliente_id_seq OWNED BY public.cliente.id;
          public          postgres    false    214            ?            1259    16848    funcionario    TABLE       CREATE TABLE public.funcionario (
    id integer NOT NULL,
    nome character varying(50) NOT NULL,
    nascimento character varying(15) NOT NULL,
    email character varying(50) NOT NULL,
    telefone character varying(15) NOT NULL,
    cargo character varying(30) NOT NULL
);
    DROP TABLE public.funcionario;
       public         heap    postgres    false            ?            1259    16847    funcionario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.funcionario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.funcionario_id_seq;
       public          postgres    false    219            X           0    0    funcionario_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.funcionario_id_seq OWNED BY public.funcionario.id;
          public          postgres    false    218            ?            1259    16921    pertence    TABLE     c   CREATE TABLE public.pertence (
    vacinaid integer NOT NULL,
    prontuarioid integer NOT NULL
);
    DROP TABLE public.pertence;
       public         heap    postgres    false            ?            1259    16873    possui    TABLE     b   CREATE TABLE public.possui (
    animalid integer NOT NULL,
    agendamentoid integer NOT NULL
);
    DROP TABLE public.possui;
       public         heap    postgres    false            ?            1259    16898 
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
       public         heap    postgres    false            ?            1259    16897    prontuario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.prontuario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.prontuario_id_seq;
       public          postgres    false    226            Y           0    0    prontuario_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.prontuario_id_seq OWNED BY public.prontuario.id;
          public          postgres    false    225            ?            1259    16915    vacina    TABLE     ?   CREATE TABLE public.vacina (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    validade character varying(10) NOT NULL,
    fabricante character varying(150) NOT NULL,
    volume character varying(15) NOT NULL
);
    DROP TABLE public.vacina;
       public         heap    postgres    false            ?            1259    16914    vacina_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.vacina_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.vacina_id_seq;
       public          postgres    false    228            Z           0    0    vacina_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.vacina_id_seq OWNED BY public.vacina.id;
          public          postgres    false    227            ?            1259    16887    veterinario    TABLE     D  CREATE TABLE public.veterinario (
    id integer NOT NULL,
    nome character varying(100) NOT NULL,
    cpf character varying(11) NOT NULL,
    nascimento character varying(10) NOT NULL,
    telefone character varying(12) NOT NULL,
    email character varying(100) NOT NULL,
    formacao character varying(100) NOT NULL
);
    DROP TABLE public.veterinario;
       public         heap    postgres    false            ?            1259    16886    veterinario_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.veterinario_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.veterinario_id_seq;
       public          postgres    false    224            [           0    0    veterinario_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.veterinario_id_seq OWNED BY public.veterinario.id;
          public          postgres    false    223            ?           2604    25151    agendamento id    DEFAULT     p   ALTER TABLE ONLY public.agendamento ALTER COLUMN id SET DEFAULT nextval('public.agendamento_id_seq'::regclass);
 =   ALTER TABLE public.agendamento ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            ?           2604    25152 	   animal id    DEFAULT     f   ALTER TABLE ONLY public.animal ALTER COLUMN id SET DEFAULT nextval('public.animal_id_seq'::regclass);
 8   ALTER TABLE public.animal ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            ?           2604    25153 
   cliente id    DEFAULT     h   ALTER TABLE ONLY public.cliente ALTER COLUMN id SET DEFAULT nextval('public.cliente_id_seq'::regclass);
 9   ALTER TABLE public.cliente ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            ?           2604    25154    funcionario id    DEFAULT     p   ALTER TABLE ONLY public.funcionario ALTER COLUMN id SET DEFAULT nextval('public.funcionario_id_seq'::regclass);
 =   ALTER TABLE public.funcionario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219            ?           2604    25155    prontuario id    DEFAULT     n   ALTER TABLE ONLY public.prontuario ALTER COLUMN id SET DEFAULT nextval('public.prontuario_id_seq'::regclass);
 <   ALTER TABLE public.prontuario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            ?           2604    25156 	   vacina id    DEFAULT     f   ALTER TABLE ONLY public.vacina ALTER COLUMN id SET DEFAULT nextval('public.vacina_id_seq'::regclass);
 8   ALTER TABLE public.vacina ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227    228            ?           2604    25157    veterinario id    DEFAULT     p   ALTER TABLE ONLY public.veterinario ALTER COLUMN id SET DEFAULT nextval('public.veterinario_id_seq'::regclass);
 =   ALTER TABLE public.veterinario ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            F          0    16855    agendamento 
   TABLE DATA           `   COPY public.agendamento (id, "observação", animalid, funcionarioid, dia, momento) FROM stdin;
    public          postgres    false    221   ?R       B          0    16813    animal 
   TABLE DATA           \   COPY public.animal (id, nome, especie, sexo, raca, peso, nascimento, clienteid) FROM stdin;
    public          postgres    false    217   ?R       @          0    16802    cliente 
   TABLE DATA           b   COPY public.cliente (id, nome, cpf, nascimento, telefone, email, rua, bairro, numero) FROM stdin;
    public          postgres    false    215   ?R       D          0    16848    funcionario 
   TABLE DATA           S   COPY public.funcionario (id, nome, nascimento, email, telefone, cargo) FROM stdin;
    public          postgres    false    219   S       N          0    16921    pertence 
   TABLE DATA           :   COPY public.pertence (vacinaid, prontuarioid) FROM stdin;
    public          postgres    false    229   oS       G          0    16873    possui 
   TABLE DATA           9   COPY public.possui (animalid, agendamentoid) FROM stdin;
    public          postgres    false    222   ?S       K          0    16898 
   prontuario 
   TABLE DATA           c   COPY public.prontuario (id, raca, data, especie, porte, sexo, animalid, veterinarioid) FROM stdin;
    public          postgres    false    226   ?S       M          0    16915    vacina 
   TABLE DATA           H   COPY public.vacina (id, nome, validade, fabricante, volume) FROM stdin;
    public          postgres    false    228   ?S       I          0    16887    veterinario 
   TABLE DATA           [   COPY public.veterinario (id, nome, cpf, nascimento, telefone, email, formacao) FROM stdin;
    public          postgres    false    224   T       \           0    0    agendamento_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.agendamento_id_seq', 19, true);
          public          postgres    false    220            ]           0    0    animal_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.animal_id_seq', 7, true);
          public          postgres    false    216            ^           0    0    cliente_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.cliente_id_seq', 49, true);
          public          postgres    false    214            _           0    0    funcionario_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.funcionario_id_seq', 8, true);
          public          postgres    false    218            `           0    0    prontuario_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.prontuario_id_seq', 5, true);
          public          postgres    false    225            a           0    0    vacina_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.vacina_id_seq', 4, true);
          public          postgres    false    227            b           0    0    veterinario_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.veterinario_id_seq', 3, true);
          public          postgres    false    223            ?           2606    16862    agendamento agendamento_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT agendamento_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT agendamento_pkey;
       public            postgres    false    221            ?           2606    16818    animal animal_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.animal DROP CONSTRAINT animal_pkey;
       public            postgres    false    217            ?           2606    16948    cliente cliente_cpf_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_cpf_key UNIQUE (cpf);
 A   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_cpf_key;
       public            postgres    false    215            ?           2606    16950    cliente cliente_email_key 
   CONSTRAINT     U   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_email_key UNIQUE (email);
 C   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_email_key;
       public            postgres    false    215            ?           2606    16807    cliente cliente_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pkey;
       public            postgres    false    215            ?           2606    16853    funcionario funcionario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.funcionario
    ADD CONSTRAINT funcionario_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.funcionario DROP CONSTRAINT funcionario_pkey;
       public            postgres    false    219            ?           2606    16903    prontuario prontuario_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT prontuario_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT prontuario_pkey;
       public            postgres    false    226            ?           2606    16920    vacina vacina_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.vacina
    ADD CONSTRAINT vacina_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.vacina DROP CONSTRAINT vacina_pkey;
       public            postgres    false    228            ?           2606    16894    veterinario veterinario_cpf_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_cpf_key UNIQUE (cpf);
 I   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_cpf_key;
       public            postgres    false    224            ?           2606    16896 !   veterinario veterinario_email_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_email_key UNIQUE (email);
 K   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_email_key;
       public            postgres    false    224            ?           2606    16892    veterinario veterinario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.veterinario
    ADD CONSTRAINT veterinario_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.veterinario DROP CONSTRAINT veterinario_pkey;
       public            postgres    false    224            ?           2606    16881    possui id_fk_agendamento    FK CONSTRAINT     ?   ALTER TABLE ONLY public.possui
    ADD CONSTRAINT id_fk_agendamento FOREIGN KEY (agendamentoid) REFERENCES public.agendamento(id) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.possui DROP CONSTRAINT id_fk_agendamento;
       public          postgres    false    3229    222    221            ?           2606    16863    agendamento id_fk_animal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT id_fk_animal FOREIGN KEY (animalid) REFERENCES public.animal(id) ON DELETE CASCADE;
 B   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT id_fk_animal;
       public          postgres    false    217    221    3225            ?           2606    16876    possui id_fk_animal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.possui
    ADD CONSTRAINT id_fk_animal FOREIGN KEY (animalid) REFERENCES public.animal(id) ON DELETE CASCADE;
 =   ALTER TABLE ONLY public.possui DROP CONSTRAINT id_fk_animal;
       public          postgres    false    3225    217    222            ?           2606    16904    prontuario id_fk_animal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT id_fk_animal FOREIGN KEY (animalid) REFERENCES public.animal(id) ON DELETE CASCADE;
 A   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT id_fk_animal;
       public          postgres    false    226    217    3225            ?           2606    16819    animal id_fk_cliente    FK CONSTRAINT     ?   ALTER TABLE ONLY public.animal
    ADD CONSTRAINT id_fk_cliente FOREIGN KEY (clienteid) REFERENCES public.cliente(id) ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.animal DROP CONSTRAINT id_fk_cliente;
       public          postgres    false    3223    217    215            ?           2606    16868    agendamento id_fk_funcionario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.agendamento
    ADD CONSTRAINT id_fk_funcionario FOREIGN KEY (funcionarioid) REFERENCES public.funcionario(id) ON DELETE CASCADE;
 G   ALTER TABLE ONLY public.agendamento DROP CONSTRAINT id_fk_funcionario;
       public          postgres    false    219    221    3227            ?           2606    16929    pertence id_fk_prontuario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.pertence
    ADD CONSTRAINT id_fk_prontuario FOREIGN KEY (prontuarioid) REFERENCES public.prontuario(id) ON DELETE CASCADE;
 C   ALTER TABLE ONLY public.pertence DROP CONSTRAINT id_fk_prontuario;
       public          postgres    false    229    226    3237            ?           2606    16924    pertence id_fk_vacina    FK CONSTRAINT     ?   ALTER TABLE ONLY public.pertence
    ADD CONSTRAINT id_fk_vacina FOREIGN KEY (vacinaid) REFERENCES public.vacina(id) ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.pertence DROP CONSTRAINT id_fk_vacina;
       public          postgres    false    228    229    3239            ?           2606    16909    prontuario id_fk_veterinario    FK CONSTRAINT     ?   ALTER TABLE ONLY public.prontuario
    ADD CONSTRAINT id_fk_veterinario FOREIGN KEY (veterinarioid) REFERENCES public.veterinario(id) ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.prontuario DROP CONSTRAINT id_fk_veterinario;
       public          postgres    false    3235    224    226            F      x?????? ? ?      B      x?????? ? ?      @   P   x?e?K
?0???],I?㸩?B?)z?;f;??z5?~$?2????՘??z?+b?y??i?RoF??q??G??VGD7?.      D   E   x???tṊ?I?4200?50"?d??Cjnbf?^r~.???????????1?[bUj?BQbfY"W? b ?      N      x?????? ? ?      G      x?????? ? ?      K      x?????? ? ?      M   F   x?3?K???K?4202?50"N0??Ș˔?9?(?/?,1(ol ?? ?p?p???ē8??b???? {R      I   ^   x?U?1
?0F?9?K%S????p	"*T:???:H?Oi???FÀ?	)'??RLRy4=]?RrٌA?????RO^D????&????s??/@??     