DROP TYPE IF EXISTS sex_en;
CREATE TYPE sex_en AS ENUM ('M', 'F');
DROP TYPE IF EXISTS ethnicity_en;
CREATE TYPE ethnicity_en AS ENUM ('Indígena', 'Afrocolombiana', 'Rom o Gitana', 'None');
DROP TYPE IF EXISTS headquarter_en;
CREATE TYPE headquarter_en AS ENUM ('Amazonia', 'Caribe', 'Bogotá', 'Manizales', 'Medellín', 'Orinoquia', 'Palmira', 'Tumaco', 'La Paz.');
DROP TYPE IF EXISTS faculty_en;
CREATE TYPE faculty_en AS ENUM ('Facultad de Ciencias Agrarias', 'Facultad de Ciencias Económicas', 'Facultad de Ciencias Humanas', 'Facultad de Ciencias', 'Facultad de Ciencias Agropecuarias', 'Facultad de Derecho, Ciencias Políticas y Sociales', 'Facultad de Ingeniería', 'Facultad de Medicina', 'Facultad de Minas', 'Facultad de Odontología', 'Facultad de Enfermería', 'Facultad de Arquitectura', 'Facultad de Artes', 'Facultad de Ciencias Administrativas');

DROP TYPE IF EXISTS major_en;
CREATE TYPE major_en AS ENUM (
    'Ingeniería de Sistemas y Computación','Ingeniería de Sistemas e Informática', 'Ingeniería Civil','Ingeniería Industrial',
    'Ingeniería Electrónica', 'Ingeniería Eléctrica', 'Ingeniería Mecánica', 'Ingeniería Mecatrónica',
    'Ingeniería Química', 'Ingeniería Agrícola', 'Ingeniería Agroindustrial', 'Ingeniería Agronómica',
    'Ingeniería Geológica', 'Ingeniería Forestal', 'Ingeniería de Minas y Metalurgia', 'Ingeniería de Petróleos',
    'Ingeniería Administrativa', 'Ingeniería Ambiental', 'Ingeniería de Control','Economía', 'Administración de Empresas', 'Contaduría Pública',
    'Derecho', 'Medicina', 'Odontología', 'Enfermería', 'Psicología', 'Arquitectura', 'Biología', 'Química',
    'Física','Matemáticas','Estadística','Geología','Geografía','Sociología','Trabajo Social','Antropología',
    'Historia','Lingüística','Literatura','Comunicación Social','Filosofía','Música','Música Instrumental','Diseño Industrial',
    'Biología Marina','Medicina Veterinaria','Zootecnia','Artes Plásticas','Ciencias Política','Ciencias de la Computación',
    'Cine y Televisión','Diseño Gráfico','Español y Filología Clásica','Farmacia','Filología e Idiomas: Alemán',
    'Filología e Idiomas: Francés','Filología e Idiomas: Inglés','Fisioterapia','Nutrición y Dietética','Gestión Cultural y Comunicativa',
    'Administración de Sistemas Informáticos','Construcción'
);

DROP TYPE IF EXISTS dependence_en;
CREATE TYPE dependence_en AS ENUM ('ORI', 'DRE');
DROP TYPE IF EXISTS region_en;
CREATE TYPE region_en AS ENUM ('Norte América', 'Latinoamérica','Europa','Oceanía','Uniandes','Convenio Sigueme/Nacional');
DROP TYPE IF EXISTS format_en;
CREATE TYPE format_en AS ENUM ('Presencial', 'Virtual', 'Mixto');
DROP TYPE IF EXISTS study_level_en;
CREATE TYPE study_level_en AS ENUM ('Pregrado', 'Postgrado', 'Doctorado');
DROP TYPE IF EXISTS language_en;
CREATE TYPE language_en AS ENUM ('Inglés', 'Español', 'Francés', 'Portugés', 'Alemán', 'Italiano', 'Koreano', 'Ruso', 'Chino', 'Otro');
DROP TYPE IF EXISTS semester_en;
CREATE TYPE semester_en AS ENUM ('1', '2');
DROP TYPE IF EXISTS admission_en;
CREATE TYPE admission_en AS ENUM ('Regular', 'PAES', 'PEAMA');