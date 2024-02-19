import streamlit as st


def calculate_wavelengths(series, start, end):
    # Constants
    R = 1.097e-2  # Rydberg constant in nm^-1

    # Calculate wavelengths
    wavelengths = []
    for n in range(start, end + 1):
        wavelength = 1 / (R * (1 / 4 - 1 / n ** 2))
        wavelengths.append(wavelength)

    return wavelengths


st.title('Hydrogen Spectral Lines')

series = st.selectbox('Select a series:', ['Balmer', 'Paschen', 'Pfund'])

if series == 'Balmer':
    start, end = 3, 6
elif series == 'Paschen':
    start, end = 4, 7
elif series == 'Pfund':
    start, end = 5, 8

wavelengths = calculate_wavelengths(series, start, end)

st.write(f'### {series} Series')

for n, wavelength in zip(range(start, end + 1), wavelengths):
    st.write(f'n = {n}: {wavelength:.2f} nm')

