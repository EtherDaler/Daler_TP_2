#include "A/index.h"
#include "B/lib.h"
#include <iostream>
#include "gtest/gtest.h"

class CRectTest : public ::testing::Test {
};


TEST(CRectTest, delta)
{
        EXPECT_EQ(1, delta(2,1));
        EXPECT_EQ(6, delta(5,-1));

}

TEST(CRectTest, multiply){
        EXPECT_EQ(2, mult(2,1));
        EXPECT_EQ(-5, mult(5,-1));
}
