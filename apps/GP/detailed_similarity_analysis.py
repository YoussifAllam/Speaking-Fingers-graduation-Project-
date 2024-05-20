import numpy as np


def detailed_similarity_analysis_and_feedback(reference, hypothesis):
    # Matrix initialization for dynamic programming
    d = np.zeros((len(reference) + 1, len(hypothesis) + 1))
    for i in range(len(reference) + 1):
        for j in range(len(hypothesis) + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][0] = i
            else:
                substitution_cost = 0 if reference[i-1] == hypothesis[j-1] else 1
                d[i][j] = min(d[i-1][j] + 1,  # deletion
                              d[i][j-1] + 1,  # insertion
                              d[i-1][j-1] + substitution_cost)  # substitution

    # Backtracking for error analysis
    i, j = len(reference), len(hypothesis)
    operations = []
    while i > 0 and j > 0:
        current = d[i][j]
        if reference[i-1] == hypothesis[j-1]:
            i, j = i-1, j-1
            continue
        if d[i-1][j-1] + 1 == current:  # Substitution
            operations.append(('Substitution', reference[i-1], hypothesis[j-1], i-1))
            i, j = i-1, j-1
        elif d[i-1][j] + 1 == current:  # Deletion
            operations.append(('Deletion', reference[i-1], '-', i-1))
            i -= 1
        elif d[i][j-1] + 1 == current:  # Insertion
            operations.append(('Insertion', '-', hypothesis[j-1], j-1))
            j -= 1
    operations.reverse()

    # Calculate similarity as a percentage
    cer = d[len(reference)][len(hypothesis)] / len(reference)
    similarity = (1 - cer) * 100

    # Providing feedback based on the similarity score
    feedback = ""
    if similarity > 90:
        feedback = "Excellent pronunciation! Keep it up."
    elif similarity > 70:
        feedback = "Good pronunciation, but there's room for improvement."
    elif similarity > 50:
        feedback = "Fair pronunciation. Practice will make it better."
    else:
        feedback = "Needs improvement. Keep practicing and focus on the problematic areas."

    return similarity, operations, feedback




