# Grazer
Feed me data so I can produce good result

## Summary
Grazer is a python library to be used on large data management and data analysis.

The basic idea is to feed the library with as many data as possible and let the library do most of the hard work for you, data comparison or data analysis


## Usage

>grazer = Grazer()
>
>data = grazer.generate_data('THE FISHIN COMPANY') // returns data object
>data.add_metadaata('know_address', '. 3714 MAIN STREET, PITTSBURGH PA 151 20 US')
>data.add_metadaata('products', 'FROZEN TILAPIA FILLET')
>data.add_metadaata('products', 'FROZEN TILAPIA')
>data.add_metadaata('products', 'TILAPIA FILLET')
>
>data2 = grazer.generate_data('FISHIN COMPANY THE')
>data2.add_metadaata('know_address', '. 3714 MAIN STREET, PITTSBURGH PA 151 20 US')
>data2.add_metadaata('products', 'FROZEN TILAPIA FILLET')
>data2.add_metadaata('products', 'FROZEN TILAPIA')
>data2.add_metadaata('products', 'TILAPIA FILLET')
>data2.add_metadaata('products', 'FILLET')
>data2.add_metadaata('products', 'TILAPIA')
>
>grazer.add_data(data)
>grazer.add_data(data2) // should be intelligent enough to merge the 2 data
>
>data3 = grazer.generate_data('FISH COMPANY')
>data3.add_metadaata('know_address', '. 3714 MAIN STREET, PITTSBURGH PA 151 20 US')
>data3.add_metadaata('products', 'FROZEN TILAPIA FILLET')
>data3.add_metadaata('products', 'FROZEN TILAPIA')
>data3.add_metadaata('products', 'TILAPIA FILLET')
>data3.add_metadaata('products', 'FILLET')
>data3.add_metadaata('products', 'TILAPIA')
>
>grazer.find_similar_data(data3)
>grazer.merge_data('THE FISHIN COMPANY', data3)