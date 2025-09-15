<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Assignment #2 - Python & PHP</title>
</head>
<body>
    <h1>IST105 - Dynamic Content with Python and PHP</h1>
    <h2>Equation Calculator</h2>
    <p>Equation: Result = b + (√(c³)/a) * 10</p>

    <form action="index.php" method="get">
        <label for="a">Value for a:</label>
        <input type="number" step="any" id="a" name="a" required value="<?php echo isset($_GET['a']) ? htmlspecialchars($_GET['a']) : ''; ?>">
        <br><br>
        <label for="b">Value for b:</label>
        <input type="number" step="any" id="b" name="b" required value="<?php echo isset($_GET['b']) ? htmlspecialchars($_GET['b']) : ''; ?>">
        <br><br>
        <label for="c">Value for c:</label>
        <input type="number" step="any" id="c" name="c" required value="<?php echo isset($_GET['c']) ? htmlspecialchars($_GET['c']) : ''; ?>">
        <br><br>
        <input type="submit" value="Calculate">
    </form>

    <hr>

    <?php
    // Check if the variables were sent via GET
    if (isset($_GET['a']) && isset($_GET['b']) && isset($_GET['c'])) {
        // Build the query string for the Python script
        $queryString = http_build_query([
            'a' => $_GET['a'],
            'b' => $_GET['b'],
            'c' => $_GET['c']
        ]);

        // Set the QUERY_STRING environment variable so the Python cgi script can read it
        putenv("QUERY_STRING=$queryString");

        // Full path to the executable Python script
        $command = '/var/www/html/calculate.py';

        // Execute the command and capture the output
        $output = shell_exec($command);

        // Display the result
        echo "<h2>Calculation Result:</h2>";
        echo "<pre style='font-family: monospace; font-size: 16px;'>$output</pre>";
    }
    ?>
</body>
</html>