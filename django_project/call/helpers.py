from student.models import Student
from application.models import Application

from .models import Call, University


def update_data(data, row, value):
    if data[row][0] == -1:
        data[row][0] = value
        data[row][1] = value
    else:
        data[row][0] = min(data[row][0], value)
        data[row][1] = max(data[row][1], value)


def get_info_statistics(data_call: str, data_student: str) -> dict:
    """
    Returns a dictionary with the statistics solicited (data_call vs data_student) with the following
    format:

    For tables:
        [
            {'university': 'UNAL', 'males': 50, 'females': 40},
            {'university': 'UNIANDES', 'males': 30, 'females': 40}
        ]

    For candle sticks:
        [
            {'university': 'UNAL', 'min': 45, 'max': 80},
            {'university': 'UNIANDES', 'min': 15, 'max': 90},
        ]
    """
    # Set the names of the rows
    if data_call == 'university':
        rows = {university.name: i for i, university in enumerate(University.objects.all())}
    elif data_call == 'country':
        countries = set(university.country for university in University.objects.all())
        rows = {country: i for i, country in enumerate(countries)}
    elif data_call == 'region':
        rows = {display: i for i, (_, display) in enumerate(getattr(University, f'region_choices'))}
    elif data_call == 'semester':
        rows = {display: i for i, (_, display) in enumerate(getattr(Call, f'semester_choices'))}
    else:
        raise NotImplemented(f'{data_call} not implemented yet')

    # Types of data_call that will be shown with tables
    data_table = ['faculty', 'major', 'sex', 'admission', 'study_level']

    # Set the name of the columns (in the candle sticks only min and max is used)
    type_chart = 'table' if data_student in data_table else 'candle'
    if type_chart == 'table':
        columns = {
            str(display): i for i, (_, display) in enumerate(getattr(Student, f'{data_student}_choices'))
        }
        data_applications = [[0 for _ in range(len(columns))] for _ in range(len(rows))]
        data_winners = [[0 for _ in range(len(columns))] for _ in range(len(rows))]
    else:
        columns = {
            word: i for i, word in enumerate(['min', 'max'])
        }
        data_applications = [[-1, -1] for _ in range(len(rows))]
        data_winners = [[-1, -1] for _ in range(len(rows))]

    # Fill data
    for application in Application.objects.all():
        if data_call == 'university':
            r = application.call.university.name
        elif data_call == 'country':
            r = application.call.university.country
        elif data_call == 'region':
            r = application.call.university.get_region_display()
        else:
            r = application.call.get_semester_display()

        row = rows[r]

        if type_chart == 'table':
            col = columns[getattr(application.student, f'get_{data_student}_display')()]
            data_applications[row][col] += 1
            if application.approved:
                data_winners[row][col] += 1

        else:
            value = getattr(application.student, data_student)
            update_data(data_applications, row, value)
            if application.approved:
                update_data(data_winners, row, value)

    # Set the display values used for rows and columns
    display_rows = list(range(len(rows)))
    for value, row in rows.items():
        display_rows[row] = value

    display_columns = list(range(len(columns)))
    for value, column in columns.items():
        display_columns[column] = value

    # Set the info of the applications and the winners with the output needed by the front
    info_applications = []
    for display_row, row in zip(display_rows, data_applications):
        data = {data_call: display_row}
        for display_column, value in zip(display_columns, row):
            data[display_column] = value
        info_applications.append(data)

    info_winners = []
    for display_row, row in zip(display_rows, data_winners):
        data = {data_call: display_row}
        for display_column, value in zip(display_columns, row):
            data[display_column] = value
        info_winners.append(data)

    output = {
        'type_chart': type_chart,
        'postulates': info_applications,
        'winners': info_winners,
    }

    return output
