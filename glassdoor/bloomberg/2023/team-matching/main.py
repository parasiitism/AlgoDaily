"""
    Employees rank Teams and teams rank employees, find the best matches
    
    e.g.

    Input:
    employee_preferences = {employeeA: [Team1, Team2], employeeB: [Team2, Team1]}
    team_preferences = {team1: [A, B], team2:[A, B]}

    Output:
    A: [team 1]
    B: [team 2]

    ==== Solution ====

    Stable Marriage Problem (aka. Gale-Shapley Algorithm)
    - https://www.youtube.com/watch?v=0m_YW1zVs-Q
"""


def team_matching(employee_preferences, team_preferences):

    matches = {}  # { team: employee }
    unmatched_employees = []
    for employee in employee_preferences:
        unmatched_employees.append(employee)

    while len(unmatched_employees) > 0:
        employee = unmatched_employees.pop(0)

        empl_perf = employee_preferences[employee]
        first_team = empl_perf.pop()

        if first_team not in matches:
            matches[first_team] = employee
        else:
            cur_member = matches[first_team]
            team_pref = team_preferences[first_team]

            if team_pref.index(employee) < team_pref.index(cur_member):
                unmatched_employees.append(cur_member)
                matches[first_team] = employee
            else:
                unmatched_employees.append(employee)

    return matches


a = {
    "A": ["team1", "team2"],
    "B": ["team2", "team1"],
}
b = {
    "team1": ["A", "B"],
    "team2": ["A", "B"],
}
print(team_matching(a, b))  # {'team2': 'A', 'team1': 'B'}

print("-----")


def team_matching2(employee_preferences, team_preferences):

    matches = {}  # { employee: team }
    unmatched_teams = []
    for t in team_preferences:
        unmatched_teams.append(t)

    while len(unmatched_teams) > 0:
        team = unmatched_teams.pop(0)

        team_perf = team_preferences[team]
        first_employee = team_perf.pop()

        if first_employee not in matches:
            matches[first_employee] = team
        else:
            cur_team = matches[first_employee]
            employee_pref = employee_preferences[first_employee]

            if employee_pref.index(team) < employee_pref.index(cur_team):
                unmatched_teams.append(cur_team)
                matches[first_employee] = team  # replace the current partner
            else:
                unmatched_teams.append(team)  # put the 'team' back to the q

    return matches


a = {
    "A": ["team1", "team2"],
    "B": ["team2", "team1"],
}
b = {
    "team1": ["A", "B"],
    "team2": ["A", "B"],
}
print(team_matching2(a, b))
