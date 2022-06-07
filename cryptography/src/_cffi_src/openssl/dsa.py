# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


INCLUDES = """
#include <openssl/dsa.h>
"""

TYPES = """
typedef ... DSA;
"""

FUNCTIONS = """
int DSA_generate_key(DSA *);
DSA *DSA_new(void);
void DSA_free(DSA *);
DSA *DSAparams_dup(DSA *);
int DSA_size(const DSA *);
int DSA_sign(int, const unsigned char *, size_t, unsigned char *, unsigned int *,
             DSA *);
int DSA_verify(int, const unsigned char *, size_t, const unsigned char *, size_t,
               DSA *);

/* added in 1.1.0 to access the opaque struct */
void DSA_get0_pqg(const DSA *, const BIGNUM **, const BIGNUM **,
                  const BIGNUM **);
int DSA_set0_pqg(DSA *, BIGNUM *, BIGNUM *, BIGNUM *);
void DSA_get0_key(const DSA *, const BIGNUM **, const BIGNUM **);
int DSA_set0_key(DSA *, BIGNUM *, BIGNUM *);
int DSA_generate_parameters_ex(DSA *, unsigned, unsigned char *, size_t,
                               int *, unsigned long *, BN_GENCB *);
"""

CUSTOMIZATIONS = """
"""
