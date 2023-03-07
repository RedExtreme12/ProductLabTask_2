import openpyxl


def get_articles_to_process(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active

    articles_to_process = [row[0] for row in ws.iter_rows(values_only=True, max_col=1)]
    return articles_to_process
