import streamlit as st

st.set_page_config(page_title="Bruno Figueroa - Perfil Profesional", page_icon="📦", layout="centered")

# Encabezado
st.title("BRUNO EMANUEL FIGUEROA")
st.subheader("Operario de Logística | Control de Stock | Desarrollador de Software")
st.divider()

# Perfil
st.header("Perfil Profesional")
st.write("""
Operario con amplia experiencia en logística, depósito, reposición y control de stock. 
Especializado en la gestión de sector frío de supermercados mayoristas, realizando control de existencias, 
inventarios físicos y digitales, rotación FIFO y recepción de mercadería. 
Cuento con conocimientos avanzados de Excel aplicados a control de stock, desarrollo de software en Python 
para automatización de depósitos y formación activa en ERP SAP (Módulo MM).
""")

# Habilidades
st.header("Habilidades Clave")
col1, col2 = st.columns(2)

with col1:
    st.write("**Operativa de Depósito & Logística:**")
    st.success("• Control de Stock")
    st.success("• Inventario Físico / Digital")
    st.success("• Sector Frío & Rotación FIFO")
    st.success("• Picking, Embalaje y Palletizado")

with col2:
    st.write("**Sistemas & Tecnología:**")
    st.warning("• Excel Avanzado")
    st.warning("• Programación Python (Streamlit / PyQt5)")
    st.warning("• ERP SAP MM (En formación)")
    st.warning("• Mantenimiento y Reparación de PC")

# Proyecto Destacado
st.header("Proyecto Destacado")
st.info("""
**Software de Control de Stock:** Sistema desarrollado en **Python / Streamlit** enfocado en la gestión operativa de depósitos. 
Incluye desglose automático de unidades por cajón/bulto, trazabilidad de vencimientos y generación de reportes inmediatos.
""")

# Experiencia Laboral
st.header("Experiencia Laboral")
st.write("**Mayorista Limón — Repositor / Control de Stock (Sector Frío)** | 2026 – Actualidad")
st.write("Registro de entradas/salidas, inventarios, rotación FIFO, armados de pallets y control de stock mediante Excel.")

st.write("**Ave Caesar — Ayudante de Cocina** | 2025 – 2026")
st.write("Preparación de alimentos, recepción de mercadería, control de vencimientos y rotación FIFO.")

st.write("**Autoservicio La Italiana — Repositor / Fiambrería** | 2021 – 2024")
st.write("Control de vencimientos, pesaje, rotulación de productos y atención al cliente.")

st.divider()

# Contacto
st.header("Contacto Directo")
st.write("📍 **Ubicación:** Merlo / Zona Oeste - Buenos Aires")
st.write("📱 **WhatsApp:** 11-2356-8530")
st.write("✉️ **Email:** bf05100@gmail.com")

st.link_button("Hablar por WhatsApp", "https://wa.me/541123568530")