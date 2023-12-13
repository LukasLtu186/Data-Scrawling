import tabula

tables = tabula.read_pdf("ast_sci_data_tables_sample.pdf", pages="all" )
# print(tables)
df = tables[1] # data frame
print(type(df))
print(df)
print()
print(df[df.Car == "Spirit of America"])
