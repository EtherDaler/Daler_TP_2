#include "main_test.h"

TEST(CRectTest, delta)
{
        EXPECT_EQ(1, delta(2,1));
        EXPECT_EQ(6, delta(5,-1));

}

TEST(CRectTest, multiply){
        EXPECT_EQ(2, mult(2,1));
        EXPECT_EQ(-5, mult(5,-1));
}

int main(int argc, char **argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
