from Table import Table

table = Table()
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])

print(table)

table.add_rows(
                [
                    ["Sydney", 2058, 4336374, 1214.8],
                    ["Melbourne", 1566, 3806092, 646.9],
                    ["Perth", 5386, 1554769, 869.4],
                ]
            )

print(table)

table.del_row(2)
print(table)

table.del_column("Area")
print(table)