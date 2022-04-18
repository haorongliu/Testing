from math import radians
from random import randint, random


def total_count( list_total ):

                result_report = 1
                total_record  = 1
                
                for num_per_line in list_total:
                
                    if ( result_report % 10 ) == 0:
                        
                        print( num_per_line )
                        result_report += 1
                    
                    else:

                        print( num_per_line, end=" " )
                        result_report += 1 
                
                for i in list_total:
                    
                    for j in list_total:
                        
                        if i==j:
                            
                            total_record += 1
                    
                    print ( ("[{}: {}] ".format(i,total_record)),end="" )
                    total_record=0                
                
                print( "" )

def final_count( Total_silver,Total_gold,Total_iron ):

                print( " How much silver you got: {}\n How much gold you got:{}\n How much iron you got:{}".format( Total_silver,Total_gold,Total_iron ) )


def main_one( num_banner ):
    try:

        num_banner = int( num_banner )

        while num_banner != ( -1 ):
            
            Silver_count = 1
            Gold_count   = 1
            list_total   = []
            random_one   = 0
            Total_count  = 0
            Total_silver = 0
            Total_gold   = 0
            Total_iron   = 0

            for numbers in range( num_banner ):

                random_numb=randint( 0,int( 99 ) )

                if ( 5 <= random_numb <= 10 ) or ( Silver_count == 10 ):
                    
                    random_one = randint( 0,9 )
                    list_total.append( silver[ random_one ] )
                    Silver_count  = 1
                    Gold_count   += 1
                    random_one    = 0
                    Total_silver += 1
                    Total_count  += 1
                
                elif ( random_numb < ( 0.5 ) ) or ( Gold_count == 90 ):
                    
                    random_one=randint( 0,1 )
                    
                    if random_one == 0:
                    
                        list_total.append( gold[ random_one ] )
                    
                    elif random_one != 0:
                        
                        random_two = randint( 0,2 )    
                        list_total.append( gold[ random_one ][ random_two ] )
                    
                    Gold_count   = 1
                    random_one   = 0
                    Total_gold  += 1
                    Total_count += 1

                else:
                    
                    random_one = randint( 0,9 )
                    list_total.append( iron[ random_one ] )
                    Silver_count += 1
                    Gold_count   += 1
                    random_one    = 0
                    Total_iron   += 1  
                    Total_count  += 1   
            
            total_count( list_total )
            final_count( Total_silver, Total_gold, Total_iron )
                    
            if Total_count == num_banner:

                print( "" )
                num_banner = ( input( "Please enter how much you want to banner:" ) )
                main_one( num_banner )
    
    except ValueError:

        print( "Enter valid number" )
        num_banner = ( input( "Please enter how much you want to banner:" ) )
        main_one( num_banner )


if __name__ == "__main__":

    silver=["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"]
    gold=["g1",["g2","g3","g4"]]
    iron=["i1","i2","i3","i4","i5","i6","i7","i8","i9","i10"]

    num_banner= input( "Please enter how much you want to banner:" )
    main_one(num_banner)