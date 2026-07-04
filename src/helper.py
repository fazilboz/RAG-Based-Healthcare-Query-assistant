import os


def load_pdf_files(folder):

    pdfs = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            pdfs.append(
                os.path.join(folder, file)
            )

    return pdfs