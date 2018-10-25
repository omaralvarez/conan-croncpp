#include <iostream>
#include <chrono>
#include <thread>

#include <croncpp/croncpp.h>

int main()
{

    try
    {

        auto cron = cron::make_cron("*/5 * * * * *");
        
        std::time_t now = std::time(0);
        std::time_t next = cron::cron_next(cron, now);

        std::cout << next << std::endl;

        std::this_thread::sleep_for(std::chrono::seconds(3));   
        
        now = std::time(0);
        next = cron::cron_next(cron, now);

        std::cout << next << std::endl;

    }
    catch (cron::bad_cronexpr const & ex)
    {

        std::cerr << ex.what() << '\n';

    }
    
}