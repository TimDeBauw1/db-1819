def query_01(connection, column_names):
    
    # Bouw je query
    query="""
    SELECT t.name, t.yearID, t.HR 
    FROM Teams as t
    ORDER BY t.HR DESC;
    """.format()
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df

def query_02(connection, column_names, datum_x='1980-01-16'):
    
    # Bouw je query
    query="""
    SELECT m.nameFirst, m.nameLast, m.birthYear, m.birthMonth, m.birthDay
    FROM Master as m
    WHERE debut > {} 
    ORDER BY m.nameLast ASC;
    """.format(datum_x)
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df

def query_03(connection, column_names):
    
    # Bouw je query
    query="""
    SELECT DISTINCT t2.nameFirst, t2.nameLast, t1.teamID
    FROM (SELECT playerId,teamID FROM Managers m WHERE m.plyrMgr = 'N') as t1, 
        (SELECT playerID, nameFirst, nameLast FROM Master) as t2 
    WHERE  t1.playerId = t2.playerID
    ORDER BY t1.teamID
    """
    
    # Stap 2 & 3
    res = run_query(connection, query)         # Query uitvoeren
    df = res_to_df(res, column_names)          # Query in DataFrame brengen
    
    return df

