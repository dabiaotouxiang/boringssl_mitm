# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


INCLUDES = """
#include <openssl/err.h>
"""

TYPES = """
static const int EVP_F_EVP_ENCRYPTFINAL_EX;
static const int EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH;
static const int EVP_R_BAD_DECRYPT;
static const int EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM;
static const int PKCS12_R_PKCS12_CIPHERFINAL_ERROR;
static const int PEM_R_UNSUPPORTED_ENCRYPTION;
//static const int EVP_R_UNKNOWN_PBE_ALGORITHM;

static const int ERR_LIB_EVP;
static const int ERR_LIB_PEM;
static const int ERR_LIB_ASN1;
static const int ERR_LIB_PKCS12;

static const int SSL_TLSEXT_ERR_OK;
static const int SSL_TLSEXT_ERR_ALERT_FATAL;
static const int SSL_TLSEXT_ERR_NOACK;

static const int X509_R_CERT_ALREADY_IN_HASH_TABLE;
"""

FUNCTIONS = """
void ERR_error_string_n(uint32_t, char *, size_t);
const char *ERR_lib_error_string(uint32_t);
const char *ERR_func_error_string(uint32_t);
const char *ERR_reason_error_string(uint32_t);
unsigned long ERR_get_error(void);
unsigned long ERR_peek_error(void);
void ERR_clear_error(void);
void ERR_put_error(int, int, int, const char *, unsigned);

int ERR_GET_LIB(unsigned long);
int ERR_GET_FUNC(unsigned long);
int ERR_GET_REASON(unsigned long);

"""

CUSTOMIZATIONS = """
# define EVP_F_EVP_ENCRYPTFINAL_EX                        127
# define EVP_R_BAD_DECRYPT                                100
# define EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH          138
# define EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM          118
# define PKCS12_R_PKCS12_CIPHERFINAL_ERROR                116
# define ERR_LIB_PKCS12          35
"""
