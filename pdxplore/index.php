
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>pdXplore</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    
<?php 
    echo nl2br("Listing all events by date \n\n");
    $strJsonFileContents = file_get_contents('./../json/events-json.txt');
    $events_array = json_decode($strJsonFileContents, TRUE);
    // echo nl2br( date("m/d/y", strtotime("2011/01/07"))."\n" );
    // echo ( date("m/d/y", strtotime("11/01/07")) <=> date("m/d/y", strtotime("11/01/06")) )."<br>";
    $total_num_events = count( $events_array['events'] );
    
    // var_dump( $events_array['events'] );
    $all_events = $events_array['events'];
    usort( $all_events, function($x, $y){        
        return date("m/d/y", strtotime( substr( $x['event-dates'], 0, 8 ) )) <=> date( "m/d/y", strtotime( substr( $y['event-dates'], 0, 8 ) ) );
    } );
    // var_dump( $events );
    foreach ($all_events as $key => $event_entry) {
        $red = 'green';
        // echo $event_entry['event-dates'].'</br>';
        $is_on_multiple_days = strpos( $event_entry['event-dates'], "," );
        // echo $is_on_multiple_days ? "many dates" : "single date";
        $event_page = $event_entry['event-page'];
        if ($is_on_multiple_days) {
            $first_show_date = substr( $event_entry['event-dates'], 0, 8 );
            $additional_days = substr_count( $event_entry['event-dates'], "," );
            echo '<div>'.'<a href="'.$event_page.'">'.$event_entry['event'].'</a>'.' | '.$event_entry['event-venue'].' | '.$first_show_date." (Also playing for the next $additional_days days)</div>";
            echo '</br>';
        }
        else {
            echo '<div>'.'<a href="'.$event_page.'">'.$event_entry['event'].'</a>'.' | '.$event_entry['event-venue'].' | '.$event_entry['event-dates'].'</div>';
            echo '</br>';
        }
    }
?>
    
</body>
</html>
