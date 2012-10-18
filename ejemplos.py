from pyDB import *

f=CDF()
f.from_parse("p_numero->p_recaudacion p_hora p_fecha p_estadio p_publico_presente p_n_fecha,a_cuil->a_nombre,e_nombre e_ciudad->e_calle e_numero e_capacidad,c_nombre c_ciudad->c_escudo e_nombre e_ciudad,j_cuil->j_nombre j_edad j_desde j_hasta j_posicion j_n_camiseta c_nombre c_ciudad,en_cuil->en_nombre en_edad en_desde en_hasta en_matricula c_nombre c_ciudad,pf_cuil->pf_nombre pf_edad pf_desde pf_hasta c_nombre c_ciudad,m_cuil->m_nombre m_edad m_desde m_hasta m_matricula c_nombre c_ciudad,p_numero g_minuto g_tiempo->j_cuil,p_numero t_minuto t_tiempo->j_cuil,p_numero ca_minuto ca_tiempo->j_cuil ca_j_cuil,a_cuil p_numero->d_funcion,p_numero j_cuil->j_titular_suplente,e_nombre e_ciudad->c_nombre c_ciudad,j_cuil->e_nombre e_ciudad e_calle e_numero e_capacidad,en_cuil->e_nombre e_ciudad e_calle e_numero e_capacidad,pf_cuil->e_nombre e_ciudad e_calle e_numero e_capacidad,m_cuil->e_nombre e_ciudad e_calle e_numero e_capacidad,ca_j_cuil->c_nombre c_ciudad","a_cuil,a_nombre,c_ciudad,c_escudo,c_nombre,ca_j_cuil,ca_minuto,ca_tiempo,d_funcion,e_calle,e_capacidad,e_ciudad,e_nombre,e_numero,en_cuil,en_desde,en_edad,en_hasta,en_matricula,en_nombre,g_minuto,g_tiempo,j_cuil,j_desde,j_edad,j_hasta,j_n_camiseta,j_nombre,j_posicion,j_titular_suplente,m_cuil,m_desde,m_edad,m_hasta,m_matricula,m_nombre,p_estadio,p_fecha,p_hora,p_n_fecha,p_numero,p_publico_presente,p_recaudacion,pf_cuil,pf_desde,pf_edad,pf_hasta,pf_nombre,t_color,t_minuto,t_tiempo")
print str(f)
c=f.fnbc()

print "Forma Normal de Boyce Codd= "
c=[str(x) for x in c]
c.sort()
for i in c:
    print i
print len(c)
