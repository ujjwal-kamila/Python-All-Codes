class InvalidQuestionAnswerFileFormat(Exception):
    pass

def check_file_validity(file_name):
    try:
        with open(file_name, 'r') as file:
            questions = []
            answers = []

            for line in file:
                line = line.strip()
                if line.startswith('Q'):
                    questions.append(line)
                elif line.startswith('A'):
                    answers.append(line)
                elif line != "":
                    raise InvalidQuestionAnswerFileFormat("Invalid file format")

            if len(questions) != len(answers):
                raise InvalidQuestionAnswerFileFormat("Number of questions and answers do not match")
            
            return True

    except FileNotFoundError:
        print("File not found")
        return False
    except InvalidQuestionAnswerFileFormat as e:
        print(e)
        return False

# Test the function
file_name = 'QandA.txt'
if check_file_validity(file_name):
    print(True)
