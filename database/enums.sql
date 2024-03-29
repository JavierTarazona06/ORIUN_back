DROP TYPE IF EXISTS sex_en CASCADE;
CREATE TYPE sex_en AS ENUM ('m', 'f');

DROP TYPE IF EXISTS ethnicity_en CASCADE;
CREATE TYPE ethnicity_en AS ENUM ('indígena', 'afrocolombiana', 'Rom o Gitana', 'None');

DROP TYPE IF EXISTS headquarter_en CASCADE;
CREATE TYPE headquarter_en AS ENUM ('Amazonia', 'Caribe', 'Bogotá', 'Manizales', 'Medellín', 'Orinoquia', 'Palmira', 'Tumaco', 'La Paz.');

DROP TYPE IF EXISTS faculty_en CASCADE;
CREATE TYPE faculty_en AS ENUM ('Facultad de Ciencias Agrarias', 'Facultad de Ciencias Económicas', 'Facultad de Ciencias Humanas', 'Facultad de Ciencias', 'Facultad de Ciencias Agropecuarias', 'Facultad de Derecho, Ciencias Políticas y Sociales', 'Facultad de Ingeniería', 'Facultad de Medicina', 'Facultad de Minas', 'Facultad de Odontología', 'Facultad de Enfermería', 'Facultad de Arquitectura', 'Facultad de Artes', 'Facultad de Ciencias de la Educación', 'Facultad de Ciencias Administrativas');

DROP TYPE IF EXISTS major_en CASCADE;
CREATE TYPE major_en AS ENUM ('Ingeniería de Sistemas y Computación', 'Ingeniería Civil', 'Ingeniería Industrial', 'Ingeniería Electrónica', 'Ingeniería Mecánica', 'Ingeniería Química', 'Ingeniería de Alimentos', 'Ingeniería Agronómica', 'Economía', 'Administración de Empresas', 'Contaduría Pública', 'Derecho', 'Medicina', 'Odontología', 'Enfermería', 'Psicología', 'Arquitectura', 'Biología', 'Química', 'Física', 'Matemáticas', 'Estadística', 'Geología', 'Geografía', 'Sociología', 'Trabajo Social', 'Antropología', 'Historia', 'Lingüística', 'Literatura', 'Comunicación Social', 'Filosofía', 'Música', 'Diseño Industrial', 'Ingeniería Ambiental', 'Biología Marina', 'Microbiología', 'Genética', 'Astronomía', 'Medicina Veterinaria', 'Agronomía', 'Zootecnia', 'Medicina Veterinaria y Zootecnia', 'Ingeniería de Materiales', 'Ingeniería Eléctrica', 'Ingeniería de Telecomunicaciones', 'Ingeniería Biomédica', 'Ingeniería Forestal', 'Ingeniería Sanitaria', 'Ingeniería Geológica', 'Ingeniería de Minas', 'Ingeniería de Petróleos', 'Ingeniería de Producción', 'Ingeniería de Topografía', 'Ingeniería Catastral y Geodesia', 'Ingeniería Ambiental y Sanitaria', 'Ingeniería de Transporte', 'Ingeniería Agrícola', 'Ingeniería Agroindustrial');

DROP TYPE IF EXISTS dependence_en CASCADE;
CREATE TYPE dependence_en AS ENUM ('ORI', 'DRE');

DROP TYPE IF EXISTS region_en CASCADE;
CREATE TYPE region_en AS ENUM ('Norte América', 'Latinoamérica','Europa','Oceanía','Uniandes','Convenio Sigueme/Nacional');

DROP TYPE IF EXISTS format_en CASCADE;
CREATE TYPE format_en AS ENUM ('Presencial', 'Virtual', 'Mixto');

DROP TYPE IF EXISTS study_level_en CASCADE;
CREATE TYPE study_level_en AS ENUM ('Pregrado', 'Postgrado');

DROP TYPE IF EXISTS language_en CASCADE;
CREATE TYPE language_en AS ENUM ('Inglés', 'Español', 'Francés', 'Portugés', 'Alemán', 'Italiano', 'Koreano', 'Ruso', 'Mandarín', 'Otro');

DROP TYPE IF EXISTS semester_en CASCADE;
CREATE TYPE semester_en AS ENUM ('1', '2');

DROP TYPE IF EXISTS admission_en CASCADE;
CREATE TYPE admission_en AS ENUM ('Regular', 'PAES', 'PEAMA');

DROP TYPE IF EXISTS doc_en CASCADE;
CREATE TYPE doc_en AS ENUM ('Cédula de ciudadanía', 'Cédula de extranjería', 'Pasaporte');