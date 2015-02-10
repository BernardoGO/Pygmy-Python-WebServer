package area;
use Exporter;

our @ISA= qw( Exporter );
our @EXPORT_OK = qw( areaOfCircle );
our @EXPORT_OK = qw( areaOfCircle );

sub areaOfCircle {
    $radius = $_[0];
    return(3.1415 * ($radius ** 2));
}

