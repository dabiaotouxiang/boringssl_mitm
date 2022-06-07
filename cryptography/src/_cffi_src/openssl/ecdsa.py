# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


INCLUDES = """
#include <openssl/ecdsa.h>
"""

TYPES = """
typedef ... ECDSA_SIG;

typedef ... CRYPTO_EX_new;
typedef ... CRYPTO_EX_dup;
typedef ... CRYPTO_EX_free;
"""

FUNCTIONS = """
int ECDSA_sign(int, const unsigned char *, size_t, unsigned char *,
               unsigned int *, EC_KEY *);
int ECDSA_verify(int, const unsigned char *, size_t, const unsigned char *, size_t,
                 EC_KEY *);
size_t ECDSA_size(const EC_KEY *);

"""

CUSTOMIZATIONS = """
typedef void CRYPTO_EX_new (void *parent, void *ptr, CRYPTO_EX_DATA *ad,
                           int idx, long argl, void *argp);
"""
