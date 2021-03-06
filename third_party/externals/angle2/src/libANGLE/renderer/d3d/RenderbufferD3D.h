//
// Copyright (c) 2014 The ANGLE Project Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
//

// RenderbufferD3d.h: Defines the RenderbufferD3D class which implements RenderbufferImpl.

#ifndef LIBANGLE_RENDERER_D3D_RENDERBUFFERD3D_H_
#define LIBANGLE_RENDERER_D3D_RENDERBUFFERD3D_H_

#include "angle_gl.h"

#include "common/angleutils.h"
#include "libANGLE/renderer/RenderbufferImpl.h"

namespace rx
{
class RendererD3D;
class RenderTarget;
class SwapChain;

class RenderbufferD3D : public RenderbufferImpl
{
  public:
    RenderbufferD3D(RendererD3D *renderer);
    virtual ~RenderbufferD3D();

    static RenderbufferD3D *makeRenderbufferD3D(RenderbufferImpl *renderbuffer);

    virtual gl::Error setStorage(GLsizei width, GLsizei height, GLenum internalformat, GLsizei samples) override;

    virtual GLenum getActualFormat() const;

    RenderTarget *getRenderTarget();
    unsigned int getRenderTargetSerial() const;

  private:
    DISALLOW_COPY_AND_ASSIGN(RenderbufferD3D);

    RendererD3D *mRenderer;
    RenderTarget *mRenderTarget;
};
}

#endif // LIBANGLE_RENDERER_D3D_RENDERBUFFERD3D_H_
