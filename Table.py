class Table:

    def __init__(self, field_names = []):
        self.field_names = field_names
        self.rows = []

    # adds a single row to the table (rows)
    def add_row(self, new_row):
        self.rows.append(new_row)

    # adds a few rows to the table (rows)
    def add_rows(self, new_rows):
        self.rows.extend(new_rows)

    # adds a column to the table (rows)
    def add_column(self, field_name, column_datas):

        # appends the field naem to update the field names attribute
        self.field_names.append(field_name)

        # if the table (rows) is empty, add in column data in a list
        # to create a multidimensional list
        if len(self.rows) == 0:
            for column_data in column_datas:
                self.rows.append([column_data])
        else:
            for index in range(len(self.rows)):
                self.rows[index].append(column_datas[index])

    # deletes the specified row based on the index (target)
    def del_row(self, target):
        del self.rows[target]

    # deletes the sepcified column based on the name of the column name (target)
    def del_column(self, target):

        target_index = 0
        found = False

        # finds the index of the specified column (target)
        for index in range(len(self.field_names)):
            if self.field_names[index] == target:
                target_index = index
                found = True
                break

        if found == True:
            del self.field_names[target_index]
            for row in self.rows:
                del row[target_index]

    # clears all the rows in the table except the field_names
    def clear_rows(self):
        self.rows = []

    # clears everything
    def clear(self):
        self.field_names = []
        self.rows = []

    # get column values based on the specified field name
    def get_column(self, target):

        target_index = 0
        found = False
        for index in range(len(self.field_names)):
            if self.field_names[index] == target:
                target_index = index
                found = True
                break

        column = []

        if found != False:
            for row in self.rows:
                column.append(row[target_index])
            return column
        else:
            return column

    # acts as a toString for the table
    def get_string(self, fields = None, start = None, end = None):

        if fields == None:
            fields = self.field_names

        if start == None or end == None:
            start = 0
            end = len(self.rows)

        # start: gets maximum width for each column
        max_widths = []

        for field_name in fields:

            # gets all data for specified column
            column = self.get_column(field_name)

            # initialises the field name as the maximum width
            max_width = len(field_name)

            # converts all the columns data to string
            str_column = [str(data) for data in column]

            # loops through the str_column and find the maximum width
            for data in str_column:
                if len(data) > max_width:
                    max_width = len(data)

            # appends max width once it has been found for each column
            max_widths.append(max_width)
        # end: gets maximum width for each column

        # initialises empty string
        output = ""

        # start: creates the line seperator
        # which is something like this: +--+--+
        line = "+"
        for max_width in max_widths:

            # to ensure it is | Age | instead of |Age| but for ---
            # note: this is for the ---- to be evenly spaced out
            line += "-" * (max_width + 2) + "+"
        # end: creates the line seperator

        # start: creates the header (field names)
        # initialses as "+---+---+\n"
        header = line + "\n"

        # creates | Name | Age |
        for index in range(len(fields)):

            field_name = fields[index]

            spaces = " " * (max_widths[index] - len(field_name))

            header += "| " + field_name + spaces + " "

        # adds the ending "|\n", "+--+--+", "\n"
        header += "|\n" + line + "\n"

        output += header
        # end: creates the header (field names)

        # start: finds the actual index of the specified fields
        columns_index = []
        for index in range(len(fields)):
            for n_index in range(len(self.field_names)):
                if fields[index] == self.field_names[n_index]:
                    columns_index.append(n_index)
                    break

        if len(columns_index) == 0:
            return "None"
        # end: finds the actual index of the specified fields

        # start: gets the rest of the data for each row
        for row in range(start, end):

            # initialses temp_column for max_widths index to prevent index out of bound
            temp_column = 0
            for column in columns_index:

                # gets the data for that specific row and column from the table
                data = str(self.rows[row][column])

                spaces = " " * (max_widths[temp_column] - len(data))

                output += "| " + data + spaces + " "

                temp_column += 1

            # adds "|", "\n" for next row consisting of datas
            output += "|\n"

        if len(self.rows) != 0:
            output += line
        # end: gets the rest of the data for each row

        return output

    # overrides toString method
    def __str__(self):
        return self.get_string()