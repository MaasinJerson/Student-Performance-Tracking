# Array (list) to store student data
students_array = []

# Function to insert or update student scores and store in an array
def insert_or_update_student_array(student_id, student_name, scores):
    """
    Insert or update a student's scores in the students_array.
    
    Args:
    student_id (str): The ID of the student.
    student_name (str): The name of the student.
    scores (dict): A dictionary containing the student's scores across assessments.
    """
    # Check if the student already exists
    for student in students_array:
        if student['id'] == student_id:
            student['name'] = student_name
            student['scores'] = scores
            return f"Student {student_name} (ID: {student_id}) updated successfully."

    # If the student does not exist, insert them
    students_array.append({
        'id': student_id,
        'name': student_name,
        'scores': scores
    })
    return f"Student {student_name} (ID: {student_id}) added successfully."


# Function to search for a student by ID number
def search_student_by_id(student_id):
    """
    Search for a student by their ID number.
    
    Args:
    student_id (str): The ID of the student to search for.
    
    Returns:
    dict or str: The student's data if found, otherwise a 'not found' message.
    """
    for student in students_array:
        if student['id'] == student_id:
            return student
    return f"Student with ID {student_id} not found."


# Function to calculate the prefix sum array for a student's scores
def calculate_prefix_sum(scores):
    """
    Calculate the prefix sum array for a list of student scores.
    
    Args:
    scores (list): A list of scores from assessments.
    
    Returns:
    list: A prefix sum array.
    """
    prefix_sum = []
    cumulative_sum = 0
    for score in scores:
        cumulative_sum += score
        prefix_sum.append(cumulative_sum)
    return prefix_sum


# Function to check if a student is passing based on average score
def check_if_passing(student_id, passing_threshold=60):
    """
    Check if the student is passing or failing based on their average score.
    
    Args:
    student_id (str): The ID of the student.
    passing_threshold (int): The minimum average score required to pass (default is 60).
    
    Returns:
    str: A message stating whether the student is passing or failing.
    """
    student = search_student_by_id(student_id)
    if isinstance(student, str):  # If student is not found, return the error message
        return student
    
    # Retrieve the student's scores
    scores = student['scores']
    
    # Calculate the total score and the number of assessments
    total_score = sum(scores.values())
    num_assessments = len(scores)
    
    # Calculate the average score
    average_score = total_score / num_assessments
    
    # Check if the student is passing or failing
    if average_score >= passing_threshold:
        return f"Student {student['name']} (ID: {student_id}) is passing with an average score of {average_score:.2f}%."
    else:
        return f"Student {student['name']} (ID: {student_id}) is failing with an average score of {average_score:.2f}%."


# Function to calculate the sum of scores between two assessments using the prefix sum array
def range_query(prefix_sum, start_index, end_index):
    """
    Calculate the sum of scores between two assessments using the prefix sum array.
    
    Args:
    prefix_sum (list): A prefix sum array.
    start_index (int): The starting index of the assessment range.
    end_index (int): The ending index of the assessment range.
    
    Returns:
    int: The sum of the scores in the given range.
    """
    if start_index == 0:
        return prefix_sum[end_index]
    else:
        return prefix_sum[end_index] - prefix_sum[start_index - 1]


# Example: Insert 10 sample students with both passing and failing students into the array
sample_student_data_10 = [
    {'id': '1111111-1', 'name': 'John Doe', 'scores': {
        'Class Participation': 82,
        'Assignment': 75,
        'Quiz #1': 85,
        'Quiz #2': 95,
        'Quiz #3': 78,
        'Midterm Exam': 88}},  
    
    {'id': '1111111-2', 'name': 'Jane Smith', 'scores': {
        'Class Participation': 50,
        'Assignment': 55,
        'Quiz #1': 40,
        'Quiz #2': 45,
        'Quiz #3': 35,
        'Midterm Exam': 48}},  
    
    {'id': '1111111-3', 'name': 'Mike Johnson', 'scores': {
        'Class Participation': 78,
        'Assignment': 82,
        'Quiz #1': 79,
        'Quiz #2': 88,
        'Quiz #3': 90,
        'Midterm Exam': 85}},  
    
    {'id': '1111111-4', 'name': 'Emily Davis', 'scores': {
        'Class Participation': 64,
        'Assignment': 60,
        'Quiz #1': 62,
        'Quiz #2': 68,
        'Quiz #3': 70,
        'Midterm Exam': 66}},  
    
    {'id': '1111111-5', 'name': 'David Wilson', 'scores': {
        'Class Participation': 48,
        'Assignment': 45,
        'Quiz #1': 50,
        'Quiz #2': 52,
        'Quiz #3': 40,
        'Midterm Exam': 55}},  
    
    {'id': '1111111-6', 'name': 'Sophia Brown', 'scores': {
        'Class Participation': 89,
        'Assignment': 92,
        'Quiz #1': 88,
        'Quiz #2': 94,
        'Quiz #3': 85,
        'Midterm Exam': 90}},  
    
    {'id': '1111111-7', 'name': 'Chris White', 'scores': {
        'Class Participation': 56,
        'Assignment': 54,
        'Quiz #1': 60,
        'Quiz #2': 63,
        'Quiz #3': 58,
        'Midterm Exam': 61}},  
    
    {'id': '1111111-8', 'name': 'Olivia Martinez', 'scores': {
        'Class Participation': 91,
        'Assignment': 89,
        'Quiz #1': 95,
        'Quiz #2': 94,
        'Quiz #3': 90,
        'Midterm Exam': 96}},  
    
    {'id': '1111111-9', 'name': 'Liam Anderson', 'scores': {
        'Class Participation': 42,
        'Assignment': 38,
        'Quiz #1': 40,
        'Quiz #2': 45,
        'Quiz #3': 43,
        'Midterm Exam': 47}},  
    
    {'id': '1111111-10', 'name': 'Ava Thompson', 'scores': {
        'Class Participation': 72,
        'Assignment': 70,
        'Quiz #1': 78,
        'Quiz #2': 80,
        'Quiz #3': 76,
        'Midterm Exam': 82}}  
]

# Insert the sample data into the students_array
students_array = []  # Reset the array
for data in sample_student_data_10:
    insert_or_update_student_array(data['id'], data['name'], data['scores'])

# Display the passing and failing status for each student
passing_status_list = []
for student in students_array:
    passing_status = check_if_passing(student['id'])
    passing_status_list.append(passing_status)

# Output the passing status list
for status in passing_status_list:
    print(status)

# Example of using prefix sum and range queries for cumulative score calculation:
student = search_student_by_id('1111111-1')  # John Doe
scores_list = list(student['scores'].values())  # Extract the list of scores
prefix_sum = calculate_prefix_sum(scores_list)

