/*
 * =====================================================================================
 *
 *       Filename:  crack.c
 *
 *    Description:  crack passcode for python
 *
 *        Version:  1.0
 *        Created:  04/04/2014 15:26:17
 *       Compiler:  gcc
 *
 *         Author:  JiaDi Yue (Brady), jdyue19@gmail.com
 *
 * =====================================================================================
 */
#include <openssl/evp.h>
#include <string.h>

#define KEK_KEY_LEN  20
#define ITERATION    1000 

char * crack_thread(char *key, char * salt, char *pass_code) {
    unsigned char out[41];
    char pass[5];
    int i;
    //for(i = 0; i < 10000; i++) {
    for(i = 0; i < 10000; i++) {
        sprintf(pass, "%04d", i);
        PKCS5_PBKDF2_HMAC_SHA1(pass, strlen(pass), (const unsigned char *)salt, strlen(salt), ITERATION, KEK_KEY_LEN, out);

//        printf("%04d | ", i);
//        int j;
//        for(j = 0; j < KEK_KEY_LEN; j++) { 
//            printf("%02x", out[j]); 
//        } 
//        printf("\n");

        if(memcmp((const void *)key, (const void *)out, 20))
            continue;
        else {
            strcpy(pass_code, pass);
//            printf("key: %s\n", pass);
            break;
        }
    }
    return pass_code;
}
