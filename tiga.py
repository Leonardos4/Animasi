import pandas as pd 
import streamlit as st
import numpy as np
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title='Verifikasi F3', layout="wide")

# Fungsi untuk membuat DataFrame gabungan
def copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    # Membuat DataFrame untuk periode lalulalu
    juruslalulalu = pd.DataFrame({
        'BLTH': lalulalu.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': lalulalu.get('IDPEL', pd.Series(dtype='int64')),
        'NOPEL': lalulalu.get('NOPEL', pd.Series(dtype='object')),
        'NAMA': lalulalu.get('NAMA', pd.Series(dtype='object')),
        'UNITAP': lalulalu.get('UNITAP', pd.Series(dtype='object')),
        'UNITUP': lalulalu.get('UNITUP', pd.Series(dtype='object')),
        'KODEPOSTING': lalulalu.get('KODEPOSTING', pd.Series(dtype='int64')),
        'KDKELOMPOK': lalulalu.get('KDKELOMPOK', pd.Series(dtype='object')),
        'KDPROSES': lalulalu.get('KDPROSES', pd.Series(dtype='object')),
        'KDDK': lalulalu.get('KDDK', pd.Series(dtype='object')),
        'TARIF': lalulalu.get('TARIF', pd.Series(dtype='object')),
        'DAYA': lalulalu.get('DAYA', pd.Series(dtype='float64')),
        'TG': lalulalu.get('TG', pd.Series(dtype='object')),
        'FKMKWH': lalulalu.get('FKMKWH', pd.Series(dtype='float64')),
        'FKMKVARH': lalulalu.get('FKMKVARH', pd.Series(dtype='float64')),
        'SLALWBP': lalulalu.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBPCABUT': lalulalu.get('LWBPCABUT', pd.Series(dtype='float64')),
        'LWBPPASANG': lalulalu.get('LWBPPASANG', pd.Series(dtype='float64')),
        'SAHLWBP': lalulalu.get('SAHLWBP', pd.Series(dtype='float64')),
        'LWBPPAKAI': lalulalu.get('LWBPPAKAI', pd.Series(dtype='float64')),
        'SLAWBP': lalulalu.get('SLAWBP', pd.Series(dtype='float64')),
        'THBLMUT': lalulalu.get('THBLMUT', pd.Series(dtype='object')),
        'WBPCABUT': lalulalu.get('WBPCABUT', pd.Series(dtype='float64')),
        'WBPPASANG': lalulalu.get('WBPPASANG', pd.Series(dtype='float64')),
        'SAHWBP': lalulalu.get('SAHWBP', pd.Series(dtype='float64')),
        'WBPPAKAI': lalulalu.get('WBPPAKAI', pd.Series(dtype='float64')),
        'SLAKVARH': lalulalu.get('SLAKVARH', pd.Series(dtype='float64')),
        'KVARHCABUT': lalulalu.get('KVARHCABUT', pd.Series(dtype='float64')),
        'KVARHPASANG': lalulalu.get('KVARHPASANG', pd.Series(dtype='float64')),
        'SAHKVARH': lalulalu.get('SAHKVARH', pd.Series(dtype='float64')),
        'KVARHPAKAI': lalulalu.get('KVARHPAKAI', pd.Series(dtype='float64')),
        'KELBKVARH': lalulalu.get('KELBKVARH', pd.Series(dtype='float64')),
        'KVAMAX_WBP': lalulalu.get('KVAMAX_WBP', pd.Series(dtype='float64')),
        'DAYAMAX': lalulalu.get('DAYAMAX', pd.Series(dtype='float64')),
        'DAYAMAX_WBP': lalulalu.get('DAYAMAX_WBP', pd.Series(dtype='float64')),
        'TGLBACA': lalulalu.get('TGLBACA', pd.Series(dtype='object')),
        'TGLUPLOAD': lalulalu.get('TGLUPLOAD', pd.Series(dtype='object')),
        'TGLINISIALISASI': lalulalu.get('TGLINISIALISASI', pd.Series(dtype='object')),
        'NAMAPNJ': lalulalu.get('NAMAPNJ', pd.Series(dtype='object')),
        'KODERBM': lalulalu.get('KODERBM', pd.Series(dtype='object')),
        'DLPD': lalulalu.get('DLPD', pd.Series(dtype='float64')),
        'DLPD_LM': lalulalu.get('DLPD_LM', pd.Series(dtype='float64')),
        'KDPEMBMETER': lalulalu.get('KDPEMBMETER', pd.Series(dtype='object')),
        'PTGENTRIMETER': lalulalu.get('PTGENTRIMETER', pd.Series(dtype='object')),
        'KODE_BACA': lalulalu.get('KODE_BACA', pd.Series(dtype='object')),
        'KELAINAN_BC_METER': lalulalu.get('KELAINAN_BC_METER', pd.Series(dtype='object')),
        'MSG': lalulalu.get('MSG', pd.Series(dtype='object')),
        'DLPD_FKM': lalulalu.get('DLPD_FKM', pd.Series(dtype='float64')),
        'DLPD_KVARH': lalulalu.get('DLPD_KVARH', pd.Series(dtype='float64')),
        'DLPD_3BLN': lalulalu.get('DLPD_3BLN', pd.Series(dtype='float64')),
        'DLPD_JNSMUTASI': lalulalu.get('DLPD_JNSMUTASI', pd.Series(dtype='object')),
        'DLPD_TGLBACA': lalulalu.get('DLPD_TGLBACA', pd.Series(dtype='object')),
        'ALASAN_ENTRI': lalulalu.get('ALASAN_ENTRI', pd.Series(dtype='object')),
        'ALASAN_KOREKSI': lalulalu.get('ALASAN_KOREKSI', pd.Series(dtype='object')),
        'SAHLWBP_IMPORT': lalulalu.get('SAHLWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHWBP_IMPORT': lalulalu.get('SAHWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHKVARH_IMPORT': lalulalu.get('SAHKVARH_IMPORT', pd.Series(dtype='float64'))
    })

    # Membuat DataFrame untuk periode lalu
    juruslalu = pd.DataFrame({
        'BLTH': lalu.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': lalu.get('IDPEL', pd.Series(dtype='int64')),
        'NOPEL': lalu.get('NOPEL', pd.Series(dtype='object')),
        'NAMA': lalu.get('NAMA', pd.Series(dtype='object')),
        'UNITAP': lalu.get('UNITAP', pd.Series(dtype='object')),
        'UNITUP': lalu.get('UNITUP', pd.Series(dtype='object')),
        'KODEPOSTING': lalu.get('KODEPOSTING', pd.Series(dtype='int64')),
        'KDKELOMPOK': lalu.get('KDKELOMPOK', pd.Series(dtype='object')),
        'KDPROSES': lalu.get('KDPROSES', pd.Series(dtype='object')),
        'KDDK': lalu.get('KDDK', pd.Series(dtype='object')),
        'TARIF': lalu.get('TARIF', pd.Series(dtype='object')),
        'DAYA': lalu.get('DAYA', pd.Series(dtype='float64')),
        'TG': lalu.get('TG', pd.Series(dtype='object')),
        'FKMKWH': lalu.get('FKMKWH', pd.Series(dtype='float64')),
        'FKMKVARH': lalu.get('FKMKVARH', pd.Series(dtype='float64')),
        'SLALWBP': lalu.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBPCABUT': lalu.get('LWBPCABUT', pd.Series(dtype='float64')),
        'LWBPPASANG': lalu.get('LWBPPASANG', pd.Series(dtype='float64')),
        'SAHLWBP': lalu.get('SAHLWBP', pd.Series(dtype='float64')),
        'LWBPPAKAI': lalu.get('LWBPPAKAI', pd.Series(dtype='float64')),
        'SLAWBP': lalu.get('SLAWBP', pd.Series(dtype='float64')),
        'THBLMUT': lalu.get('THBLMUT', pd.Series(dtype='object')),
        'WBPCABUT': lalu.get('WBPCABUT', pd.Series(dtype='float64')),
        'WBPPASANG': lalu.get('WBPPASANG', pd.Series(dtype='float64')),
        'SAHWBP': lalu.get('SAHWBP', pd.Series(dtype='float64')),
        'WBPPAKAI': lalu.get('WBPPAKAI', pd.Series(dtype='float64')),
        'SLAKVARH': lalu.get('SLAKVARH', pd.Series(dtype='float64')),
        'KVARHCABUT': lalu.get('KVARHCABUT', pd.Series(dtype='float64')),
        'KVARHPASANG': lalu.get('KVARHPASANG', pd.Series(dtype='float64')),
        'SAHKVARH': lalu.get('SAHKVARH', pd.Series(dtype='float64')),
        'KVARHPAKAI': lalu.get('KVARHPAKAI', pd.Series(dtype='float64')),
        'KELBKVARH': lalu.get('KELBKVARH', pd.Series(dtype='float64')),
        'KVAMAX_WBP': lalu.get('KVAMAX_WBP', pd.Series(dtype='float64')),
        'DAYAMAX': lalu.get('DAYAMAX', pd.Series(dtype='float64')),
        'DAYAMAX_WBP': lalu.get('DAYAMAX_WBP', pd.Series(dtype='float64')),
        'TGLBACA': lalu.get('TGLBACA', pd.Series(dtype='object')),
        'TGLUPLOAD': lalu.get('TGLUPLOAD', pd.Series(dtype='object')),
        'TGLINISIALISASI': lalu.get('TGLINISIALISASI', pd.Series(dtype='object')),
        'NAMAPNJ': lalu.get('NAMAPNJ', pd.Series(dtype='object')),
        'KODERBM': lalu.get('KODERBM', pd.Series(dtype='object')),
        'DLPD': lalu.get('DLPD', pd.Series(dtype='float64')),
        'DLPD_LM': lalu.get('DLPD_LM', pd.Series(dtype='float64')),
        'KDPEMBMETER': lalu.get('KDPEMBMETER', pd.Series(dtype='object')),
        'PTGENTRIMETER': lalu.get('PTGENTRIMETER', pd.Series(dtype='object')),
        'KODE_BACA': lalu.get('KODE_BACA', pd.Series(dtype='object')),
        'KELAINAN_BC_METER': lalu.get('KELAINAN_BC_METER', pd.Series(dtype='object')),
        'MSG': lalu.get('MSG', pd.Series(dtype='object')),
        'DLPD_FKM': lalu.get('DLPD_FKM', pd.Series(dtype='float64')),
        'DLPD_KVARH': lalu.get('DLPD_KVARH', pd.Series(dtype='float64')),
        'DLPD_3BLN': lalu.get('DLPD_3BLN', pd.Series(dtype='float64')),
        'DLPD_JNSMUTASI': lalu.get('DLPD_JNSMUTASI', pd.Series(dtype='object')),
        'DLPD_TGLBACA': lalu.get('DLPD_TGLBACA', pd.Series(dtype='object')),
        'ALASAN_ENTRI': lalu.get('ALASAN_ENTRI', pd.Series(dtype='object')),
        'ALASAN_KOREKSI': lalu.get('ALASAN_KOREKSI', pd.Series(dtype='object')),
        'SAHLWBP_IMPORT': lalu.get('SAHLWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHWBP_IMPORT': lalu.get('SAHWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHKVARH_IMPORT': lalu.get('SAHKVARH_IMPORT', pd.Series(dtype='float64'))
    })

    # Membuat DataFrame untuk periode akhir
    jurusakhir = pd.DataFrame({
        'BLTH': akhir.get('BLTH', pd.Series(dtype='object')),
        'IDPEL': akhir.get('IDPEL', pd.Series(dtype='int64')),
        'NOPEL': akhir.get('NOPEL', pd.Series(dtype='object')),
        'NAMA': akhir.get('NAMA', pd.Series(dtype='object')),
        'UNITAP': akhir.get('UNITAP', pd.Series(dtype='object')),
        'UNITUP': akhir.get('UNITUP', pd.Series(dtype='object')),
        'KODEPOSTING': akhir.get('KODEPOSTING', pd.Series(dtype='int64')),
        'KDKELOMPOK': akhir.get('KDKELOMPOK', pd.Series(dtype='object')),
        'KDPROSES': akhir.get('KDPROSES', pd.Series(dtype='object')),
        'KDDK': akhir.get('KDDK', pd.Series(dtype='object')),
        'TARIF': akhir.get('TARIF', pd.Series(dtype='object')),
        'DAYA': akhir.get('DAYA', pd.Series(dtype='float64')),
        'TG': akhir.get('TG', pd.Series(dtype='object')),
        'FKMKWH': akhir.get('FKMKWH', pd.Series(dtype='float64')),
        'FKMKVARH': akhir.get('FKMKVARH', pd.Series(dtype='float64')),
        'SLALWBP': akhir.get('SLALWBP', pd.Series(dtype='float64')),
        'LWBPCABUT': akhir.get('LWBPCABUT', pd.Series(dtype='float64')),
        'LWBPPASANG': akhir.get('LWBPPASANG', pd.Series(dtype='float64')),
        'SAHLWBP': akhir.get('SAHLWBP', pd.Series(dtype='float64')),
        'LWBPPAKAI': akhir.get('LWBPPAKAI', pd.Series(dtype='float64')),
        'SLAWBP': akhir.get('SLAWBP', pd.Series(dtype='float64')),
        'THBLMUT': akhir.get('THBLMUT', pd.Series(dtype='object')),
        'WBPCABUT': akhir.get('WBPCABUT', pd.Series(dtype='float64')),
        'WBPPASANG': akhir.get('WBPPASANG', pd.Series(dtype='float64')),
        'SAHWBP': akhir.get('SAHWBP', pd.Series(dtype='float64')),
        'WBPPAKAI': akhir.get('WBPPAKAI', pd.Series(dtype='float64')),
        'SLAKVARH': akhir.get('SLAKVARH', pd.Series(dtype='float64')),
        'KVARHCABUT': akhir.get('KVARHCABUT', pd.Series(dtype='float64')),
        'KVARHPASANG': akhir.get('KVARHPASANG', pd.Series(dtype='float64')),
        'SAHKVARH': akhir.get('SAHKVARH', pd.Series(dtype='float64')),
        'KVARHPAKAI': akhir.get('KVARHPAKAI', pd.Series(dtype='float64')),
        'KELBKVARH': akhir.get('KELBKVARH', pd.Series(dtype='float64')),
        'KVAMAX_WBP': akhir.get('KVAMAX_WBP', pd.Series(dtype='float64')),
        'DAYAMAX': akhir.get('DAYAMAX', pd.Series(dtype='float64')),
        'DAYAMAX_WBP': akhir.get('DAYAMAX_WBP', pd.Series(dtype='float64')),
        'TGLBACA': akhir.get('TGLBACA', pd.Series(dtype='object')),
        'TGLUPLOAD': akhir.get('TGLUPLOAD', pd.Series(dtype='object')),
        'TGLINISIALISASI': akhir.get('TGLINISIALISASI', pd.Series(dtype='object')),
        'NAMAPNJ': akhir.get('NAMAPNJ', pd.Series(dtype='object')),
        'KODERBM': akhir.get('KODERBM', pd.Series(dtype='object')),
        'DLPD': akhir.get('DLPD', pd.Series(dtype='float64')),
        'DLPD_LM': akhir.get('DLPD_LM', pd.Series(dtype='float64')),
        'KDPEMBMETER': akhir.get('KDPEMBMETER', pd.Series(dtype='object')),
        'PTGENTRIMETER': akhir.get('PTGENTRIMETER', pd.Series(dtype='object')),
        'KODE_BACA': akhir.get('KODE_BACA', pd.Series(dtype='object')),
        'KELAINAN_BC_METER': akhir.get('KELAINAN_BC_METER', pd.Series(dtype='object')),
        'MSG': akhir.get('MSG', pd.Series(dtype='object')),
        'DLPD_FKM': akhir.get('DLPD_FKM', pd.Series(dtype='float64')),
        'DLPD_KVARH': akhir.get('DLPD_KVARH', pd.Series(dtype='float64')),
        'DLPD_3BLN': akhir.get('DLPD_3BLN', pd.Series(dtype='float64')),
        'DLPD_JNSMUTASI': akhir.get('DLPD_JNSMUTASI', pd.Series(dtype='object')),
        'DLPD_TGLBACA': akhir.get('DLPD_TGLBACA', pd.Series(dtype='object')),
        'ALASAN_ENTRI': akhir.get('ALASAN_ENTRI', pd.Series(dtype='object')),
        'ALASAN_KOREKSI': akhir.get('ALASAN_KOREKSI', pd.Series(dtype='object')),
        'SAHLWBP_IMPORT': akhir.get('SAHLWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHWBP_IMPORT': akhir.get('SAHWBP_IMPORT', pd.Series(dtype='float64')),
        'SAHKVARH_IMPORT': akhir.get('SAHKVARH_IMPORT', pd.Series(dtype='float64'))
    })

    # Menggabungkan DataFrames
    kroscek_temp_1 = pd.merge(juruslalulalu, juruslalu, on='IDPEL', how='right')
    kroscek_temp = pd.merge(kroscek_temp_1, jurusakhir, on='IDPEL', how='right')

    # Definisi path untuk foto
    path_foto1 = 'https://portalapp.iconpln.co.id/acmt/DisplayBlobServlet1?idpel='
    path_foto2 = '&blth='

    # Membuat DataFrame akhir sesuai format yang diinginka
    kroscek = pd.DataFrame({
        'BLTH': blth_kini,
        'IDPEL': kroscek_temp['IDPEL'].astype(str),
        'NAMA': kroscek_temp['NAMA'],
        'TARIF': kroscek_temp['TARIF'],
        'DAYA': kroscek_temp['DAYA'],
        'SLALWBP': kroscek_temp['SLALWBP_y'],
        'LWBPCABUT': kroscek_temp['LWBPCABUT_y'],
        'SELISIH STAN BONGKAR': kroscek_temp['LWBPCABUT_y'] - kroscek_temp['SLALWBP_y'],
        'LWBP PASANG': kroscek_temp['LWBPPASANG_y'],
        'SAHLWBP': kroscek_temp['SAHLWBP_y'],
        'KWH 10': kroscek_temp['SAHLWBP_y'],  
        'KWH 09': kroscek_temp['SAHLWBP_x'],  
        'KWH 08': kroscek_temp['SAHLWBP_x'],
        'DELTA PEMKWH': kroscek_temp['SAHLWBP_y'] - kroscek_temp['SAHLWBP_x'], 
        '%': np.where(kroscek_temp['SAHLWBP_x'] == 0, '#DIV/0!', 
              ((kroscek_temp['SAHLWBP_y'] - kroscek_temp['SAHLWBP_x']) 
               / kroscek_temp['SAHLWBP_x'] * 100).map('{:.1f}%'.format)),
        'KET': np.where(kroscek_temp['SAHLWBP_y'] == 0, 'SESUAI', 'TIDAK SESUAI'),
        'DLPD': kroscek_temp['DLPD_y'],
        'FOTO AKHIR': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_kini,
        'FOTO LALU': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalu,
        'FOTO LALU2': path_foto1 + kroscek_temp['IDPEL'].astype(str) + path_foto2 + blth_lalulalu,
        'KET_KWH': np.where(kroscek_temp['SAHLWBP_y'] == 0, 'SESUAI', 'TIDAK SESUAI'),
        'TINDAK LANJUT': '',  
        'HASIL PEMERIKSAAN': '' 
    })

    # Mengonversi kolom LINK_FOTO menjadi tautan HTML yang bisa diklik
    kroscek['FOTO AKHIR'] = kroscek['FOTO AKHIR'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')
    kroscek['FOTO LALU'] = kroscek['FOTO LALU'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')
    kroscek['FOTO LALU2'] = kroscek['FOTO LALU2'].apply(lambda x: f'<a href="{x}" target="_blank">View Image</a>')

    # Mengembalikan dataframe kroscek
    return kroscek

# Function to filter and display images
def amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    criteria1 = ['L STAND MUNDUR', 'N KWH N O R M A L', 'K KWH NOL', 'C KWH < 40 JAM', 'J REKENING PECAHAN']

    amr_df = kroscek[kroscek['DLPD_KINI'].isin(criteria1)]
    amr_df = amr_df[amr_df['SELISIH 50%'].isin(["Selisih Besar"])]
    del amr_df['FOTO_LALU']
    del amr_df['FOTO_AKHIR']
    return amr_df

def maksFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    maks_df = kroscek[kroscek['DLPD_KINI'].isin(['L STAND METER MUNDUR'])]
    return maks_df

def norm1Filter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    norm1_df = kroscek[kroscek['DLPD_KINI'].isin(['N KWH N O R M A L'])]
    norm1_df = norm1_df[norm1_df['SELISIH 50%'].isin(["Selisih Besar"])]
    norm1_df = norm1_df[norm1_df['SUBS_NONSUBS'].isin(["Subs"])]
    return norm1_df

def norm2Filter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    norm2_df = kroscek[kroscek['DLPD_KINI'].isin(['N KWH N O R M A L'])]
    norm2_df = norm2_df[norm2_df['SELISIH 50%'].isin(["Selisih Besar"])]
    norm2_df = norm2_df[norm2_df['SUBS_NONSUBS'].isin(["Nonsubs"])]
    return norm2_df

def minNolFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    kroscek = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    minNol_df = kroscek[kroscek['DLPD_KINI'].isin(['K KWH NOL'])]
    minNol_df = minNol_df[minNol_df['MIN_NOL'].isin(['No'])]
    return minNol_df

def show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

# Fungsi filter lain
def show_image_norm1(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def show_image_norm2(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def show_image_minnol(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

def amrFilter(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini):
    df = copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    if df.empty:
        st.warning("No data available after applying the filter.")
        return

    # Display the DataFrame with clickable links using st.markdown
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
    
# Layout Columns
col = st.columns((1.5, 5), gap='medium')

with col[0]:
    st.header('Billing Management Application')

    # Input Bulan
    set_bulan = st.columns((0.75, 0.75, 0.75), gap='medium')
    with set_bulan[0]:
        blth_lalulalu = st.text_input('Masukkan periode bulan lalu2 (YYYYMM)')
    with set_bulan[1]:
        blth_lalu = st.text_input('Masukkan periode bulan lalu (YYYYMM)')
    with set_bulan[2]:
        blth_kini = st.text_input('Masukkan periode bulan kini (YYYYMM)')

    # File Uploader
    file_lalulalu = st.file_uploader("Upload Data 2 Periode Sebelumnya")
    file_lalu = st.file_uploader("Upload Data Periode Sebelumnya")
    file_akhir = st.file_uploader("Upload Data Periode Sekarang")

# Proses jika tombol ditekan dan file sudah diunggah
if st.button("Proses"):
    if file_lalulalu and file_lalu and file_akhir:
        lalulalu = pd.read_excel(file_lalulalu)
        lalu = pd.read_excel(file_lalu)
        akhir = pd.read_excel(file_akhir)

        # Display the DataFrame
        show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    else:
        st.warning("Mohon upload kedua file terlebih dahulu.")

# Tabs
with col[1]:
    st.markdown('#### Main')
    tabs = st.tabs(['SEMUA', 'T1-T6 DIATAS 40%', 'T1-T6 DIBAWAH 40%', 'T7 DIATAS 40%', 'T7 DIBAWAH 40%'])

    # Tab SEMUA
    with tabs[0]:
        st.write("Semua")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            st.dataframe(copyDataframe(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini))

    # Tab T1-T6 DIATAS 40%
    with tabs[1]:
        st.write("T1-T6 DIATAS 40%")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_maks(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab T1-T6 DIBAWAH 40%
    with tabs[2]:
        st.write("T1-T6 DIBAWAH 40%")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_norm1(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab T7 DIATAS 40%
    with tabs[3]:
        st.write("T7 DIATAS 40%")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_norm2(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)

    # Tab T7 DIBAWAH 40%
    with tabs[4]:
        st.write("T7 DIBAWAH 40%")
        if 'lalulalu' in locals() and 'lalu' in locals() and 'akhir' in locals():
            show_image_minnol(lalulalu, lalu, akhir, blth_lalulalu, blth_lalu, blth_kini)
    #siippp