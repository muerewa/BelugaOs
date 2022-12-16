/**
 * @file stdint.h
 * @author 
 * @brief 
 * @version 0.1.0
 * @date 16-12-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */



#ifndef _STDINT_H
#define _STDINT_H        1

typedef unsigned int            uintptr_t;

typedef signed char             int8_t;
typedef signed int              int16_t;
typedef signed long int         int32_t;
typedef signed long long int    int64_t;

typedef unsigned char           uint8_t;
typedef unsigned int            uint16_t;
typedef unsigned long int       uint32_t;
typedef unsigned long long int  uint64_t;

#if defined(__GNUC__) && defined(__SIZE_TYPE__)
typedef __SIZE_TYPE__   size_t;
#else
typedef unsigned long   size_t;
#endif

#endif // stdint.h