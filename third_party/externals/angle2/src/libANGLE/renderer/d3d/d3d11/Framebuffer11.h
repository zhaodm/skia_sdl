//
// Copyright 2014 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//

// Framebuffer11.h: Defines the Framebuffer11 class.

#ifndef LIBANGLE_RENDERER_D3D_D3D11_FRAMBUFFER11_H_
#define LIBANGLE_RENDERER_D3D_D3D11_FRAMBUFFER11_H_

#include "libANGLE/renderer/d3d/FramebufferD3D.h"

namespace rx
{
class Renderer11;

class Framebuffer11 : public FramebufferD3D
{
  public:
    Framebuffer11(Renderer11 *renderer);
    virtual ~Framebuffer11();

  private:
    Renderer11 *const mRenderer;
};

}

#endif // LIBANGLE_RENDERER_D3D_D3D11_FRAMBUFFER11_H_
