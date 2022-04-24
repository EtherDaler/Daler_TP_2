add_library(buffer SHARED buffer.cpp)

set_target_properties(buffer PROPERTIES PUBLIC_HEADER ../include/buffer.h)

install(TARGETS buffer
	RUNTIME DESTINATION bin
	LIBRARY DESTINATION lib
	PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_PREFIX}/include)
